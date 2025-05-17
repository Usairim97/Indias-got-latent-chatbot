# 🎤 India's Got Latent — AI Chatbot

**Your ultimate backstage pass to India's Got Latent!**  
This chatbot answers everything about the show — contestants, judges, scores, jokes, controversies, eliminations, highlights, and more!

---

## 🔍 What is This Project?

This is a Retrieval-Augmented Generation (RAG) based chatbot trained on a **manually curated, rare dataset** of the now-unavailable show *India's Got Latent*. It can answer deep, episode-level queries about performances, judges' feedback, funny moments, and behind-the-scenes buzz.

### ⚡ What Makes It Special?

> 📌 **X-Factor:** The dataset is the heart of this project — collected **manually** by watching each episode and noting:
- Judges names
- Individual contestant scores
- Episode highlights
- Jokes and humorous moments
- Contest outcomes  
> 🏆 *The show has now been removed from public access, making this dataset extremely rare.*

You can explore this dataset here:  
📊 **[Kaggle Dataset — India’s Got Latent](https://www.kaggle.com/datasets/musairim/indias-got-latentevery-episodes-data)**

---

## 🤖 Technologies Used

| Stack | Description |
|-------|-------------|
| **Model** | [`gemma-2b-it`](https://huggingface.co/google/gemma-2b-it) via [Groq API](https://console.groq.com/) |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` |
| **Framework** | FastAPI |
| **Vector Store** | FAISS |
| **Deployment** | [Hugging Face Space](https://huggingface.co/spaces/dndak/DO/tree/main) |
| **Frontend** | Custom HTML/CSS/JS (not open-sourced) |

---

## 🧠 How It Works

1. **Data Collection:**  
   JSON data collected manually across episodes from *India's Got Latent* show.
   
2. **Embeddings Creation:**  
   Using `MiniLM-L6-v2` to vectorize the data and store in FAISS.

3. **Query Flow:**
   - User inputs a question in the frontend.
   - Frontend calls backend API.
   - Retriever searches similar data chunks via vector similarity.
   - RAG model (`gemma-2b-it` via Groq) generates response with context.

4. **Response delivered** back to frontend.

---

## 🖼️ Preview Screenshots

### 🧠 Chatbot Page  
![Chatbot Screenshot](https://github.com/Usairim97/Indias-got-latent-chatbot/assets/your-screenshot-image-1-link)

### 🏠 Main Landing Page  
![Landing Screenshot](https://github.com/Usairim97/Indias-got-latent-chatbot/assets/your-screenshot-image-2-link)

> ⚠️ Upload these two images to your GitHub repo under `assets/` folder and replace the `your-screenshot-image-1-link` and `-2-link` above.

---

## 🚀 Live Demos

- 🔧 Backend API: [HF Spaces - Working Chatbot](https://huggingface.co/spaces/dndak/DO/tree/main)
- 📊 Dataset: [Kaggle - Full Episodes Data](https://www.kaggle.com/datasets/musairim/indias-got-latentevery-episodes-data)

---

## 📁 Folder Structure (Backend Only)

