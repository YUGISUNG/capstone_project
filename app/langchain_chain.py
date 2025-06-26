import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def run_chain(task: str, user_input: str) -> str:
    template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", "Task: {task}\n\nInput: {user_input}\n\nResult:")
    ])

    chain = template | llm
    result = chain.invoke({"task": task, "user_input": user_input})
    return result.content
