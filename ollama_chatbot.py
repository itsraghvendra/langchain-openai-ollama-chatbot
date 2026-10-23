"""Part 2: Local Q&A chatbot using Ollama and LangChain."""
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

MODEL_NAME = "llama3"

def get_answer(question, history=None):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful Q&A chatbot. Answer clearly, simply, and conversationally."),
        *([(role, message) for role, message in (history or [])]),
        ("human", "{question}")
    ])
    chain = prompt | ChatOllama(model=MODEL_NAME, temperature=0.3)
    try:
        return chain.invoke({"question": question}).content
    except Exception as exc:
        return (
            f"Ollama error: {exc}\n"
            "Check that Ollama is installed/running and that you ran: ollama pull llama3"
        )

if __name__ == "__main__":
    print("Ollama Q&A Chatbot (type 'exit' to stop)")
    history = []
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue
        answer = get_answer(question, history)
        print("\nBot:", answer)
        if not answer.startswith("Ollama error:"):
            history.extend([("human", question), ("ai", answer)])
