from http.client import HTTPException
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
# from generator import create_conversational_chain
# from retriver import create_vectorstore, create_llm
from constants import *
from generator import *
from retriver import *
from init_conf import *
from upload import *
import os
import pdfplumber
import chromadb
from langchain_community.vectorstores import chroma

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# llm = create_llm()



# @app.post("/upload")
# async def submit_file(file: Optional[UploadFile] = None, text: Optional[str] = None): 
#     try:

#         # file_path = f"/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/data/{file.filename}"
#         if not os.path.exists("uploads"):
#             os.makedirs("uploads")
        
#         file_path = os.path.join("uploads", file.filename)
#         with open(file_path, "wb") as f:
#             contents = await file.read()
#             f.write(contents)
#         abs_file_path = os.path.abspath(file_path)
        
#         vectorstore = create_vectorstore(file_path)
#         print(" file has been embedded into vectorestore")
#         contents = await file.read()
#         with open(file_path, "wb") as f:
#             f.write(contents)
#         with open(file_path, "rb") as f:
#             file_contents = f.read().decode()  
#         messagechain = create_conversational_chain(llm=llm, vectorstore=vectorstore)
#         print("file has been added to generation chain")
#         Query = f"Give me an accurate answer as a legal expert on the following question or just give me summary for the file content:{text}"
#         print(Query)
#         result = messagechain({"question": Query})
#         answer = result["answer"]
#         return {"file_contents": abs_file_path, "Answer": answer}
    
#     except Exception as e:
        # raise HTTPException(status_code=500, detail=str(e))

abs_file_path_global: Optional[str] = None
class Response (BaseModel):
      abs_file_path : str 
      file_contents : str

@app.get('/init')
def initialize():
    init()
    return {"message": "Initialization complete"}
@app.post('/upload')
async def submit_file(file: UploadFile):
    global abs_file_path_global
    if not os.path.exists("uploads"):
            os.makedirs("uploads")    
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as f:
            contents = await file.read()
            f.write(contents)
    abs_file_path = os.path.abspath(file_path)
    file_type = identify_file_type(abs_file_path)
    if file_type == 'Text file':
        with open(abs_file_path, "rb") as f:
            file_contents = f.read().decode(encoding="utf-8")
    elif file_type == 'PDF file':
        with pdfplumber.open(abs_file_path) as pdf:
            pages_text = [page.extract_text() for page in pdf.pages]
        file_contents = "\n".join(pages_text)
    else:
        file_contents = "Unknown file type"
    print(abs_file_path)
    output = upload(abs_file_path)
    print("output FINISHED")
    db_all, db_multi_qa =load(output=output)
    print("loading_finished")
    abs_file_path_global = abs_file_path 
    return Response(abs_file_path = abs_file_path, file_contents= file_contents, message = "File uploaded and embedded successfully")

@app.post('/message')
def ask(text: str):
    Query = text
    answer = generator(query= Query,abs_file_path= "/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/src/uploads/contract.pdf")
    message = answer['output']
    return {"message":  message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
