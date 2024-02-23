# retriever.py

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI

def create_vectorstore():
    load_dotenv()
    txt_file_path = os.getenv("TXT_FILE_PATH")  # Adjust this to your file path
    loader = TextLoader(file_path=txt_file_path, encoding="utf-8")
    data = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=5100, chunk_overlap=200)
    data = text_splitter.split_documents(data)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(data, embedding=embeddings)
    return vectorstore

def create_llm():
    api_key = os.getenv("OPENAI_API_KEY")  # Adjust this to your API key
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-4", max_tokens=500, api_key=api_key)
    return llm
