from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import openai
from constants import llm , memory
from retriver import retriever_func
from upload import *
from langchain import hub
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
from constants import *
from generator import *
from retriver import *
from init_conf import *
from upload import *

# def create_conversational_chain(llm, vectorstore):
#     memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
#     conversation_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         chain_type="stuff",
#         retriever=vectorstore.as_retriever(),
#         memory=memory,
#     )
#     return conversation_chain

def generator(query, abs_file_path):
    prompt = hub.pull("hwchase17/openai-tools-agent")
    print("prompt pulled")
    db_all, db_multi_qa =load(upload(file_path=abs_file_path))
    compression_retriever_reordered = retriever_func(db_all= db_all, db_multi_qa=db_multi_qa)
    print("got the files")
    tool = create_retriever_tool(
    compression_retriever_reordered,
    "search_upload_contract",
    "You are a contract advisor expert with immense knowledge and experience in the field. Answer my questions based on your knowledge and our older conversation. Do not make up answers.If you do not know the answer to a question, just say I don't know")
    tools = [tool]
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)
    print("agent initialized")
    result = agent_executor.invoke({"input": query})
    return result


