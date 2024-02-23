# main.py

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from generator import create_conversational_chain
from retriver import create_vectorstore, create_llm


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
vectorstore = create_vectorstore()


conversation_chain = create_conversational_chain(llm, vectorstore)

# Route to handle submission of text
@app.post("/submit_text/")
def submit_text(text: str = Form(...)):
    
    result = conversation_chain({"question": text})
    answer = result["answer"]
    return {"answer": answer}

# Route to handle submission of file
@app.post("/submit_file/")
async def submit_file(file: UploadFile = File(...)):
 
    answer = "This is a dummy answer for the uploaded file."
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
