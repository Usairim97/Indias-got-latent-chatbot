import os
import json
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
# Set transformers cache to local folder to avoid permission errors
os.environ["TRANSFORMERS_CACHE"] = "./cache"

def load_data(file_path: str):
    """Loads JSON data from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def prepare_documents(data):
    """Transforms JSON into a list of Document objects for vector storage."""
    documents = []

    # ✅ Properly Store Full Show Overview
    show_overview = data.get("show_overview", {})
    overview_parts = [
        f"Title: {show_overview.get('title', 'N/A')}",
        f"Description: {show_overview.get('description', 'N/A')}",
        f"Format: {show_overview.get('format', 'N/A')}",
        f"Inspiration: {show_overview.get('inspiration', 'N/A')}",
        f"Platform: {show_overview.get('platform', 'N/A')}",
        f"Host: {show_overview.get('host', 'N/A')}",
        f"Co-Host: {show_overview.get('co_host', 'N/A')}",
        f"First Aired: {show_overview.get('first_aired', 'N/A')}",
        f"Last Aired: {show_overview.get('last_aired', 'N/A')}",
        f"Total Episodes: {show_overview.get('total_episodes', 'N/A')}",
        f"Bonus Episodes: {show_overview.get('bonus_episodes', 'N/A')}",
        f"Audience Engagement: {show_overview.get('audience_engagement', 'N/A')}",
        f"Memes and Virality: {show_overview.get('memes_and_virality', 'N/A')}"
    ]

    controversies = show_overview.get("recent_controversies", [])
    controversy_text = "\n\n".join(
        [f"Incident: {c['incident']}\nDetails: {c['details']}\nStatus: {c['current_status']}" 
         for c in controversies]
    )
    overview_parts.append(f"Controversies:\n{controversy_text}")
    overview_parts.append(f"Current Status: {show_overview.get('current_status', 'N/A')}")
    overview_text = "\n\n".join([part for part in overview_parts if part.strip()])
    documents.append(Document(page_content=overview_text, metadata={"type": "Show Overview"}))

    # ✅ Store FAQ Answers as Separate Chunks
    for faq in data.get("faq_answers", []):
        question = faq.get("question", "")
        answer = faq.get("answer", "")
        if question and answer:
            faq_text = f"FAQ Question: {question}\nAnswer: {answer}"
            documents.append(Document(page_content=faq_text, metadata={"type": "FAQ"}))

    # ✅ Store Judges with their bio + episode appearances
    for judge in data.get("Judges", []):
        judge_name = judge["content"]["Judge"]
        judge_bio = judge["content"]["Info"]["Bio"]
        judge_appearance = ", ".join(judge["content"]["Info"].get("Episodes", []))
        judge_text = f"Judge: {judge_name}\nBio: {judge_bio}\nAppeared in: {judge_appearance}"
        documents.append(Document(page_content=judge_text, metadata={"type": "Judge", "name": judge_name}))

    # ✅ Store each Contestant Performance, Joke, and Miscellaneous as separate chunks
    for episode in data.get("Episodes", []):
        episode_number = episode.get("episode", "Unknown")
        for item in episode.get("content", []):
            if item["type"] == "Judge":
                judges = ", ".join(item["content"].get("Judges", []))
                judge_text = f"Episode {episode_number} Judges: {judges}"
                documents.append(Document(page_content=judge_text, metadata={"type": "Episode Judges", "episode": episode_number}))
            elif item["type"] == "Contestant":
                contestant = item["content"]
                contestant_info = (
                    f"Episode {episode_number} Contestant: {contestant['Contestant']}\n"
                    f"Performance: {contestant['Performance']}\n"
                    f"Scores: {json.dumps(contestant['Scores'])}\n"
                    f"Avg Score: {contestant['AvgScore']}\n"
                    f"Prediction: {contestant['Prediction']}\n"
                    f"Result: {contestant['Result']}"
                )
                documents.append(Document(page_content=contestant_info, metadata={"type": "Contestant", "episode": episode_number}))
            elif item["type"] == "Joke":
                joke_text = f"Episode {episode_number} Joke: {item['content']}"
                documents.append(Document(page_content=joke_text, metadata={"type": "Joke", "episode": episode_number}))
            elif item["type"] == "Miscellaneous":
                misc_text = f"Episode {episode_number} Miscellaneous: {item['content']}"
                documents.append(Document(page_content=misc_text, metadata={"type": "Miscellaneous", "episode": episode_number}))

    # ✅ Store Best Contestants (highlight_chunks)
    for chunk in data.get("highlight_chunks", []):
        title = chunk.get("title", "Highlight")
        for entry in chunk.get("content", []):
            name = entry.get("name", "Unknown")
            episode = entry.get("episode", "N/A")
            description = entry.get("description", "")
            text = f"{title} - {name} (Episode: {episode})\n{description}"
            documents.append(Document(page_content=text, metadata={"type": "Highlight", "name": name}))

    return documents


def download_and_load_model():
    """Load the SentenceTransformer model using new HuggingFaceEmbeddings path-compatible style."""
    try:
        embedding_model = HuggingFaceEmbeddings(model_name="./model")  # ✅ Use path string
        print("Model loaded successfully from local directory.")
        return embedding_model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def build_vector_store(documents, save_path="faiss_index"):
    """Builds a FAISS vector store from documents, saves it locally, and prints stored documents."""
    embedding_model = download_and_load_model()
    if embedding_model is None:
        print("Failed to load model. Exiting...")
        return None

    vector_store = FAISS.from_documents(documents, embedding_model)
    vector_store.save_local(save_path)

    print("\n🔎 Full List of Documents Stored in FAISS:\n")
    for i, doc in enumerate(documents):
        print(f"📌 Document {i+1} (Metadata: {doc.metadata}):\n{doc.page_content}")
        print("=" * 100)

    print(f"\n✅ FAISS Vector Store Created with {vector_store.index.ntotal} Documents.")
    return vector_store

if __name__ == "__main__":
    json_path = "data/Indias got latent data.json"
    data = load_data(json_path)
    documents = prepare_documents(data)
    vector_store = build_vector_store(documents)
    print(f"\n✅ Total Documents Created: {vector_store.index.ntotal}")