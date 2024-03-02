from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.retrievers.merger_retriever import MergerRetriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.document_transformers import (
    EmbeddingsClusteringFilter,
    EmbeddingsRedundantFilter,
)
from langchain.retrievers.document_compressors import DocumentCompressorPipeline
from langchain_community.document_transformers import LongContextReorder
from constants import embeddings


# def create_vectorstore(txt_file_path):
#     # txt_file_path = "/home/lillian/Documents/TenAcademy/week11/Contract-AI-Chatbot/backend/data/contract.txt"
#     loader = TextLoader(file_path=txt_file_path, encoding="utf-8")
#     data = loader.load()
#     text_splitter = CharacterTextSplitter(chunk_size=5100, chunk_overlap=200)
#     data = text_splitter.split_documents(data)
#     embeddings = OpenAIEmbeddings()
#     vectorstore = FAISS.from_documents(data, embedding=embeddings)
#     return vectorstore

# def create_llm():
#     load_dotenv()
#     api_key = os.getenv("OPENAI_API_KEY") 
#     llm = ChatOpenAI(temperature=0.7, model_name="gpt-4", max_tokens=500, api_key=api_key)
#     return llm
def retriever_func(db_all, db_multi_qa):
    retriever_all = db_all.as_retriever(
    search_type="similarity", search_kwargs={"k": 5 })
    retriever_multi_qa = db_multi_qa.as_retriever(
    search_type="mmr", search_kwargs={"k": 5})
    lotr = MergerRetriever(retrievers=[retriever_all, retriever_multi_qa])
    filter = EmbeddingsRedundantFilter(embeddings=embeddings)
    reordering = LongContextReorder()
    """Lost in the middle: Performance degrades when models 
    must access relevant information in the middle of long contexts.
    """
    pipeline = DocumentCompressorPipeline(transformers=[filter, reordering])
    
    compression_retriever_reordered = ContextualCompressionRetriever(
    base_compressor=pipeline, base_retriever=lotr,)
    return compression_retriever_reordered


