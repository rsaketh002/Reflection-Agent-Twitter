from langchain_core.prompts import  ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the users tweet. "
            "Always provide detailed recommendations, include requests for length, variety, style, etc. "
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts. "
            "Generate the best twitter post possible for user's request. "
            "If the user provides critique, respond with revised version of your previous attempts."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOpenAI(model="gpt-4o")

reflection_chain = reflection_prompt | llm
generation_chain = generation_prompt | llm