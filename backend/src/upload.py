import os
from constants import embeddings
from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma

from init_conf import init




def upload(file_path):
    type = identify_file_type(file_path)
    if type == 'Text file':
        loader = TextLoader(file_path=file_path, encoding="utf-8")
        data = loader.load()
        print("text uploaded")
        return data
    elif type == 'PDF file':    
        loader = PyPDFLoader(file_path)
        output =loader.load_and_split()
        print("pdf uploaded")
        return output
    
    
def identify_file_type(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == ".txt":
        return "Text file"
    elif file_extension == ".pdf":
        return "PDF file"
    else:
        return "Unknown file type"

def load(output):
    print("setting analayzed")
    api_key, all_mini, multi_qa_mini, client_settings = init()
    print("Setting analyzed")
    db_all = Chroma(
    collection_name= "project_all",
    persist_directory="/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/notebooks/db",
    client_settings= client_settings,
    embedding_function= all_mini,
    ).from_documents(output ,embeddings)
    print("embedded the file")
    db_multi_qa = Chroma(
    collection_name="project_store_multi",
    persist_directory="/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/notebooks/db",
    client_settings=client_settings,
    embedding_function=multi_qa_mini,
    ).from_documents(output, embeddings)
    print("second embedding finished")
    return db_all, db_multi_qa
    
