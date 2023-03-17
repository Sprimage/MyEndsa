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
I want you to act as if you are an AI assistant, with expertise in various fields.
"""
chat(seed_prompt)

response = chat("What is the capital of France?")
print(response)