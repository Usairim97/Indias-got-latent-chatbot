# 🤖 India's Got Latent – AI Chatbot

![Landing Screenshot](screenshots/Screenshot%20(343).png)
![Chatbot Screenshot](screenshots/Screenshot%20(342).png)

An AI chatbot trained on an exclusive dataset from the reality show **India's Got Latent**. This is not your average chatbot—it understands contestants, judges, episodes, controversies, jokes, and all the hilarious moments that defined the show.

---

## 📌 What Makes This Special (The X-Factor)

This project’s **core strength** lies in its **rare, manually curated dataset**, extracted by personally watching and documenting every episode of India’s Got Latent. Since the show has been taken down and is no longer publicly available, this dataset is **one of a kind**.

The dataset contains:
- Judges for every episode
- Each judge’s score for each contestant
- Contestant names and performances
- All jokes, funny moments, controversies, viral highlights
- Structured JSON format

➡️ **View the dataset on Kaggle**: [India's Got Latent Dataset](https://www.kaggle.com/datasets/musairim/indias-got-latentevery-episodes-data)

---

## 💡 Project Overview

| Section | Description |
|--------|-------------|
| 🔍 Retrieval-Augmented Generation (RAG) | Used to combine vector search + LLM |
| 🤖 LLM Used | `gemma-2b-it` via Groq API |
| 🔍 Embeddings Model | `sentence-transformers/all-MiniLM-L6-v2` |
| ⚙️ Frameworks | FastAPI, Docker |
| ☁️ Deployment | Hugging Face Spaces |
| 🧠 Backend | FAISS index + JSON + Retriever + Prompt |
| 💬 Frontend | Pure HTML/CSS/JS (mobile responsive) |

🚀 **Live Backend (Hugging Face Space)**:  
https://huggingface.co/spaces/dndak/DO

---

## 🛠️ Backend Structure

├── app.py # FastAPI app
├── requirements.txt
├── Dockerfile # Container config
├── data/
│ └── indias_got_latent_data.json # 🔥 Rare custom dataset
├── faiss_index/ # Precomputed FAISS vectors
├── model/ # Sentence Transformer model files
├── src/
│ ├── chatbot.py # Orchestration logic
│ ├── retriever.py # Semantic retrieval logic
│ └── data_preparation.py # Indexing and parsing logic

yaml
Copy
Edit

---

## 📸 Screenshots

Landing Page:

![Landing Page](screenshots/Screenshot%20(343).png)

Chatbot Interface:

![Chatbot](screenshots/Screenshot%20(342).png)

---

## 📦 Running Locally

### 1. Clone the Repo

```bash
git clone https://github.com/Usairim97/Indias-got-latent-chatbot.git
cd Indias-got-latent-chatbot
2. Create a virtual environment and install dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
pip install -r requirements.txt
3. Set up .env with your Groq API key
Create a file called .env:

ini
Copy
Edit
GROQ_API_KEY=your_api_key_here
4. Run the API
bash
Copy
Edit
uvicorn app:app --reload
🔍 How It Works
User input goes to /chat endpoint via FastAPI

The message is embedded via SentenceTransformer

A FAISS index returns the most semantically similar data chunks

The data and user message are combined and sent to the gemma-2b-it LLM via Groq API

A response is returned to the frontend

📂 Dataset Details
The dataset was created by manually:

Watching every episode of India’s Got Latent

Recording judges, contestants, scores, funny moments

Structuring it into JSON with episode-wise segmentation

This dataset is:

💎 Not available anywhere else online

🎯 Accurate, episode-specific, and diverse

🧠 Fine-tuned for deep information extraction

🔗 Kaggle Dataset: India's Got Latent Dataset

🙋‍♂️ Author
M. Usairim
17 y/o self-taught AI enthusiast from Multan, Pakistan.
Interested in real-world AI applications and building tools that matter.
This was my first-ever personal AI project—built with passion, persistence, and a lot of late nights.

📢 Feedback / Support
Feel free to open an issue or contact me on LinkedIn
I'd love to hear your thoughts or help if you're building something similar!

📄 License
MIT License. Use freely, credit appreciated.

yaml
Copy
Edit

---

### ✅ Summary of What to Do

| Step | Action |
|------|--------|
| 1️⃣ | Open `README.md` in VS Code or GitHub |
| 2️⃣ | Replace everything with the full markdown above |
| 3️⃣ | Push changes to GitHub |
| 4️⃣ | You're done! Your repo now looks 🔥 |

---

Let me know if you'd like a version with GitHub badges (stars, forks, license) or anything else added like a video demo, chatbot conversation samples, or "roadmap" section.







