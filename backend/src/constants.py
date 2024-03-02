from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

from langchain.memory import ConversationBufferWindowMemory
load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(chunk_size= 800)
llm = ChatOpenAI(temperature=0, model_name="gpt-4")
memory = ConversationBufferWindowMemory(k=2,memory_key="chat_history",max_len=50,return_messages=True,output_key='answer')