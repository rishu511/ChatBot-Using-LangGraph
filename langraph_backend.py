from langgraph.graph import StateGraph, START , END
from typing import TypedDict , Annotated
from langchain_core.messages import BaseMessage , HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()

class Chatstate(TypedDict):
    messages : Annotated[list[BaseMessage] , add_messages]




def chat_node(state : Chatstate):

    message = state['messages']
    responce = llm.invoke(message)
    return {'messages':[responce]}

checkpointer = MemorySaver()
graph = StateGraph(Chatstate)

#add nodes
graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpointer)
