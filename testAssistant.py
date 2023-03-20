
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain import LLMChain, OpenAI

from dotenv import load_dotenv
load_dotenv("secrets.env")

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm = ChatOpenAI(temperature=0)

agent_chain = initialize_agent([], llm, agent="chat-conversational-react-description", verbose=True, memory=memory)

def chat(input: str):
    return agent_chain.run(input=input)

seed_prompt = """
I want you to act as if you are an AI assistant
"""
chat(seed_prompt)

def run_chat():
    print("running function")
    user_input = input("You: ")
    response = chat(user_input)
    print(response)
    run_chat()


run_chat()