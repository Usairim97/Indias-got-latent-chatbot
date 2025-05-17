from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.chatbot import chat_with_bot  # ✅ Import your chatbot function

app = FastAPI()

# ✅ Allow CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Input schema
class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/")
def root():
    return {"message": "Backend is running"}

# ✅ Main chat route using your chatbot logic
@app.post("/chat")
async def chat(request: ChatRequest):
    response = chat_with_bot(user_query=request.message, session_id=request.session_id)
    return {"response": response}
