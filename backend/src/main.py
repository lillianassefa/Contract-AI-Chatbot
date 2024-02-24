from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from generator import create_conversational_chain
from retriver import create_vectorstore, create_llm
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnswerResponse(BaseModel):
    answer: str


llm = create_llm()

conversation_chain = None

# @app.on_event("startup")
# async def startup_event():
#     global conversation_chain
#     vectorstore_path = "/path/to/vectorstore"
#     conversation_chain = create_conversational_chain(llm, vectorstore_path)


@app.post("/submit_text/")
def submit_text(text: str = Form(...)):
    result = conversation_chain({"question": text})
    answer = result["answer"]
    return {"answer": answer}


@app.post("/submit_file/")
async def submit_file(file: UploadFile = File(...)):
    file_path = f"/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/data/{file.filename}"
    create_vectorstore(file_path)
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    with open(file_path, "rb") as f:
        file_contents = f.read().decode()  
    return {"file_contents": file_contents}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
