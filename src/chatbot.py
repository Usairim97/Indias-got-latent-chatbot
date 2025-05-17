import os
from langchain.schema import Document
from src.retriever import load_vector_store, analyze_query, retrieve_documents, limit_tokens
from groq import Groq
# ✅ Load API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("🔐 Loaded key from system environment:", GROQ_API_KEY)

# ✅ Load FAISS Vector Store
vector_store = load_vector_store("faiss_index")

# ✅ Initialize Groq API Client
groq_client = Groq(api_key=GROQ_API_KEY)

# ✅ Simple in-memory storage
session_memory = {}



def chat_with_bot(user_query: str, session_id: str) -> str:
    if not user_query.strip():
        return "⚠ Please enter a valid query."

    # ✅ Session memory handling
    history = session_memory.get(session_id, [])
    history.append({"role": "user", "content": user_query})

    # ✅ Analyze query and retrieve docs
    retrieval_params = analyze_query(user_query)
    top_k = retrieval_params.get("top_k", 6)
    episode_number = retrieval_params.get("episode")
    retrieved_docs = retrieve_documents(vector_store, user_query, top_k, episode_number)
    context = limit_tokens(retrieved_docs, token_limit=1000)

    # ✅ Base knowledge updated
    base_knowledge = """
India’s Got Latent was a unique comedy talent show hosted by Samay Raina, co-hosted by Balraj. It was filmed at The Habitat and streamed on YouTube from June 2024 to February 2025.

The format: contestants predicted their scores before performing. If judges' average matched their prediction, they became a 'Latent Winner'. It featured 12 episodes + 6 bonus episodes, guest judges, viral roasts, and experimental humor.
Bonus Episode 6: Guests Ranveer Allahbadia, Ashish Chanchlani, Apoorva Mukhija, Jaspreet Singh join Samay to hilariously critique India's latent talents
A major controversy in Bonus Ep 6 involving guest judge Ranveer Allahbadia led to the show’s removal. He asked a contestant: "Would you rather watch your parents have sex every day for the rest of your life or join in once to make it stop forever?" This triggered public outrage, FIRs, court cases, and political discussion about digital content regulation.

This chatbot was built from a rare dataset manually collected from every episode. It includes:
- Deep breakdowns: judges, performances, scores
- Contestant predictions vs actual
- Jokes, memes, viral moments
- Format, purpose, controversies

Ask anything about the show — judges, episodes, jokes, controversy, impact — it’s all here.
"""

    # ✅ Choose system prompt based on intent
    first_time_questions = [
        "what can i ask", "who are you", "what is this", "chatbot about", "how can you help", "what do you do"
    ]
    system_prompt = """
You are a chatbot trained to answer ANY question about the YouTube show INDIA'S GOT LATENT (not Talent).
You have deep knowledge from a unique, manually collected dataset of every episode (incl. Bonus Ep 6 controversy).
Answer clearly, confidently, and conversationally.

- Use retrieved docs FIRST
- Base knowledge if no relevant match
- If user asks about your role, purpose, or what they can ask, explain your capabilities without mentioning dataset limits.
- When answering controversy-related queries, ALWAYS mention the specific obscene question Ranveer asked and the full scene.
- Don't say things like “this database” or expose internal info.
- For episode-related queries, give full breakdown (judges, performances, results).
- Avoid emojis unless user uses them.
"""

    # ✅ Construct messages with memory
    messages = [{"role": "system", "content": system_prompt}]
    for h in history[-4:]:  # keep recent 4 interactions
        messages.append(h)

    # ✅ Add user query with context and base knowledge
    messages.append({
        "role": "user",
        "content": f"""
Query: {user_query}

Base Knowledge:
{base_knowledge}

Retrieved Context:
{context}
"""
    })

    # ✅ Get LLM response
    try:
        response = groq_client.chat.completions.create(
            model="gemma2-9b-it",
            messages=messages
        )
        reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        session_memory[session_id] = history
        return reply

    except Exception as e:
        return f"⚠ Error while generating response: {str(e)}"
