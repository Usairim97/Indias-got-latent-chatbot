# 🎤 India's Got Latent – AI Chatbot

Welcome to the official AI chatbot for the reality comedy show *India’s Got Latent*!  
This chatbot answers deep, episode-level questions about the show, contestants, judges, controversies, jokes, eliminations, and more — powered by Retrieval-Augmented Generation (RAG) and a rare, manually curated dataset.

<p align="center">
  <img src="screenshots/Screenshot (343).png" width="80%" alt="Chatbot Page Screenshot"/>
</p>

---

## 🚀 Live Demo

▶️ **Chat with the AI here**:  
🔗 [https://dndak--do.hf.space](https://dndak--do.hf.space) (Hosted via Hugging Face Spaces)

---

## 📦 Project Overview

This is a fully functional **end-to-end AI chatbot** system, built using:

- 🔍 **Retrieval-Augmented Generation (RAG)** pipeline
- 🤖 **Gemma 2B Instruct** model via **Groq API**
- 💬 **Sentence-Transformers (all-MiniLM-L6-v2)** for semantic embeddings
- ⚡ **FAISS** for fast vector search over episode data
- ⚙️ **FastAPI** backend serving the chatbot logic
- 🌐 **Frontend** connected via AJAX for real-time interactions

The user types a message → relevant episode data is retrieved → the LLM responds intelligently in context.

---

## 💎 X-Factor: Rare Dataset

The heart of this project lies in its exclusive dataset:

- 🎥 Manually created after watching every episode of *India’s Got Latent*
- 🎭 Includes judges, contestants, individual scores, and hilarious moments
- 📁 Episode-wise structure in JSON format — optimized for chunk-based retrieval
- 🔒 Unavailable online — YouTube has removed the original episodes, making this dataset **truly rare and valuable**

🔗 **View Dataset on Kaggle**:  
[https://www.kaggle.com/datasets/musairim/indias-got-latentevery-episodes-data](https://www.kaggle.com/datasets/musairim/indias-got-latentevery-episodes-data)

---

## 🛠️ Backend Architecture

```bash
chatbot/
├── app.py                     # FastAPI app with /chat endpoint
├── data/                      # Manually curated JSON data
├── src/
│   ├── chatbot.py             # Handles the query-response pipeline
│   ├── retriever.py           # Embedding + FAISS retrieval logic
│   └── data_preparation.py    # JSON chunking and preprocessing
├── faiss_index/               # Saved FAISS index and metadata
├── model/                     # SentenceTransformer model config
├── requirements.txt
├── Dockerfile
└── README.md
🖼️ Screenshot Preview
<p align="center"> <img src="screenshots/Screenshot (342).png" width="80%" alt="Homepage Screenshot"/> </p>
✨ Highlights
✅ Episode-Aware AI — understands specific shows, jokes, scores, and drama

💡 Real-world RAG Use Case — uses real, structured, rare data

🔥 Runs on Hugging Face Spaces — fast, lightweight deployment

🔐 No hallucination — responses are grounded in actual data

🌍 Frontend + Backend integration with zero manual refresh

🧠 How It Works (RAG Pipeline)
User sends query from frontend to backend via FastAPI

Query is embedded using all-MiniLM-L6-v2

FAISS retrieves semantically relevant chunks from the dataset

Context is sent to gemma-2b-it via Groq API

Response is returned to the user

🙋 Author
M. Usairim
17 y/o AI enthusiast from Multan, Pakistan 🇵🇰
First ever personal AI project — built with dedication, long nights, and passion.

“This project is proof that with persistence and creativity, even a solo beginner can build something impactful.”

📬 Feedback & Contact
Have suggestions, want to collaborate, or just want to say hi?
📩 Reach out on LinkedIn

📄 License
This project is open-source under the MIT License.
Use it freely, but attribution is appreciated.

