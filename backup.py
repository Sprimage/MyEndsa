
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


def run(self, input: str, *args, **kwargs):
    sanitized_input = self.sanitize_input(input)
    return super().run(sanitized_input, *args, **kwargs)

def sanitize_input(self, input: str) -> str:
    # Add input sanitization logic here
    sanitized_input = input
    return sanitized_input


def run(self, input: str, *args, **kwargs):
    response = super().run(input, *args, **kwargs)
    sanitized_response = self.sanitize_output(response)
    return sanitized_response

def sanitize_output(self, output: str) -> str:
    # Add output sanitization logic here
    sanitized_output = output
    return sanitized_output

openai_key = "your_openai_key_here"
input_sanitize = sanitize_input(openai_key=openai_key)
output_sanitize = sanitize_output(openai_key=openai_key)
agent_chain = initialize_agent([input_sanitize, output_sanitize], llm, agent="chat-conversational-react-description", verbose=True, memory=memory)

def chat(input: str):
    return agent_chain.run(input=input)

seed_prompt = """
I want you to act as if you are an AI assistant, with expertise in various fields.
"""
chat(seed_prompt)

response = chat("What is the capital of France?")
print(response)