from http.client import HTTPException
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


llm = create_llm()



@app.post("/upload")
async def submit_file(file: Optional[UploadFile] = None, text: Optional[str] = None): 
    try:

        # file_path = f"/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/data/{file.filename}"
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
        
        file_path = os.path.join("uploads", file.filename)
        with open(file_path, "wb") as f:
            contents = await file.read()
            f.write(contents)
        abs_file_path = os.path.abspath(file_path)
        
        vectorstore = create_vectorstore(file_path)
        print(" file has been embedded into vectorestore")
        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)
        with open(file_path, "rb") as f:
            file_contents = f.read().decode()  
        messagechain = create_conversational_chain(llm=llm, vectorstore=vectorstore)
        print("file has been added to generation chain")
        Query = f"Give me an accurate answer as a legal expert on the following question or just give me summary for the file content:{text}"
        print(Query)
        result = messagechain({"question": Query})
        answer = result["answer"]
        return {"file_contents": abs_file_path, "Answer": answer}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
