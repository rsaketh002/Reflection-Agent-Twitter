from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict

from chains import reflection_chain, generation_chain

from dotenv import load_dotenv
load_dotenv()

import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "Reflection-Agent"


# Define the state
class State(TypedDict):
    """State for the agent."""
    messages: Annotated[list, add_messages]

def _swap_roles(messages):
    new_messages = []
    for message in messages:
        if isinstance(message, AIMessage):
            new_messages.append(HumanMessage(content=message.content))
        else:
            new_messages.append(AIMessage(content=message.content))

    return new_messages

def generate_node(state: State):
    res = generation_chain.invoke({"messages": state["messages"]})
    return {"messages": [AIMessage(content=res.content)]}


def reflect_node(state: State):
    # Swap roles
    new_messages = _swap_roles(state["messages"])
    res = reflection_chain.invoke({"messages": new_messages})
    return {"messages": [HumanMessage(content=res.content)]}

def should_continue(state: State):
    if len(state["messages"]) > 6:
        return END
    return "reflect"

graph = StateGraph(State)

graph.add_node("reflect", reflect_node)
graph.add_node("generate", generate_node)

graph.set_entry_point("generate")
graph.add_conditional_edges("generate", should_continue)
graph.add_edge("reflect", "generate")

twitter_graph = graph.compile()
print(twitter_graph.get_graph().draw_mermaid())


if __name__ == "__main__":
    # Run the agent
    print("Running the agent...")
    state = {
        "messages": [
            HumanMessage(
                content="I want to write a tweet about the latest AI trends."
            ),
        ],
    }
    res = twitter_graph.invoke(state)
    
    print(res["messages"][-1].content)
