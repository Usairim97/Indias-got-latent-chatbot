from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from typing import List, Dict
from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import re

def load_vector_store(path="faiss_index"):
    embedding_model = HuggingFaceEmbeddings(model_name="./model")
    return FAISS.load_local(path, embedding_model, allow_dangerous_deserialization=True)

def analyze_query(query: str) -> Dict:
    query = query.lower()

    if any(kw in query for kw in ["what is the show", "describe the show", "who is the host", "how many episodes", "format", "taken down", "controversy"]):
        return {"type": "show_overview", "top_k": 3}

    if any(kw in query for kw in ["faq", "where was it", "will it return", "can i watch", "was it scripted"]):
        return {"type": "faq", "top_k": 4}

    match = re.search(r"(bonus episode|episode)\s*(\d+)", query)
    if match:
        ep_type = "bonus_episode" if "bonus" in match.group(1) else "episode"
        ep_num = match.group(2)
        return {"type": ep_type, "episode": ep_num, "top_k": 5}

    if "judge" in query:
        return {"type": "judge", "top_k": 6}

    if "contestant" in query or "performance" in query:
        return {"type": "performance", "top_k": 6}

    if "joke" in query or "roast" in query or "funny" in query:
        return {"type": "joke", "top_k": 5}

    return {"type": "general", "top_k": 6}

def retrieve_documents(vector_store: FAISS, query: str, top_k: int, episode_number=None) -> List[Document]:
    retriever = vector_store.as_retriever(search_kwargs={"k": top_k})
    query_lower = query.lower()

    results = []

    # 🔹 Inject Show Overview when it's about the show
    if any(kw in query_lower for kw in ["show", "how many episodes", "overview", "format"]):
        results += retriever.invoke("Show Overview")

    # 🔹 Inject FAQ chunks on general questions
    if any(kw in query_lower for kw in ["faq", "where was it", "return", "scripted"]):
        results += retriever.invoke("FAQ")

    # 🔹 Episode retrieval (bonus or not)
    match = re.search(r"(bonus episode|episode)\s*(\d+)", query_lower)
    if match:
        ep_type = "Bonus Episode" if "bonus" in match.group(1) else "Episode"
        ep_num = match.group(2)
        results += retriever.invoke(f"{ep_type} {ep_num}")

    # 🔹 Everything else (fallback)
    if not results:
        results = retriever.invoke(query)

    print("\n🔍 Retrieved Documents:")
    for i, doc in enumerate(results):
        print(f"📄 Chunk {i+1}: {doc.page_content[:300]}...\n")

    return results

def limit_tokens(documents: List[Document], token_limit: int = 3000) -> str:
    context = ""
    for doc in documents:
        if len(context.split()) + len(doc.page_content.split()) > token_limit:
            break
        context += f"{doc.page_content}\n"
    return context.strip()