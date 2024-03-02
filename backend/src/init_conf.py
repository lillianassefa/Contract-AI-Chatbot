import openai
import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
import chromadb

def init():
    load_dotenv()

    api_key = os.environ.get("OPENAI_API_KEY")

    all_mini = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    multi_qa_mini = HuggingFaceEmbeddings(model_name="multi-qa-MiniLM-L6-dot-v1")
    ABS_PATH = os.getcwd()
    DB_DIR = os.path.join(ABS_PATH, "db")
    print(DB_DIR)
    client_settings = chromadb.config.Settings(
    is_persistent=True,
    persist_directory= "/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/notebooks/db",
    anonymized_telemetry=False,
    )

    return api_key, all_mini, multi_qa_mini, client_settings