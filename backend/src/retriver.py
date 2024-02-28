from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

def create_vectorstore(txt_file_path):
    # txt_file_path = "/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/data/contract.txt"
    loader = TextLoader(file_path=txt_file_path, encoding="utf-8")
    data = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=5100, chunk_overlap=200)
    data = text_splitter.split_documents(data)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(data, embedding=embeddings)
    return vectorstore

def create_llm():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY") 
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-4", max_tokens=500, api_key=api_key)
    return llm
