
"""Part 1: Simple Q&A chatbot using Groq and LangChain."""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


def get_answer(question, history=None):
    """Return an answer from Groq with optional conversation history."""

    if not os.getenv("GROQ_API_KEY"):
        return "ERROR: Add your Groq API key to the .env file first."

    model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful Q&A chatbot. "
            "Answer clearly, simply, and conversationally."
        ),
        *((role, message) for role, message in (history or [])),
        ("human", "{question}")
    ])

    chain = prompt | model

    try:
        return chain.invoke({"question": question}).content
    except Exception as exc:
        return f"Groq error: {exc}"


if __name__ == "__main__":
    print("Groq Q&A Chatbot (type 'exit' to stop)")

    history = []

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        if not question:
            continue

        answer = get_answer(question, history)
        print("\nBot:", answer)

        if not answer.startswith("ERROR:"):
            history.extend([
                ("human", question),
                ("ai", answer)
            ])
