
"""Part 3: Streamlit chatbot with Groq/Ollama model switching."""

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

load_dotenv()

st.set_page_config(page_title="Q&A Chatbot", page_icon="💬")
st.title("💬 Q&A Chatbot")
st.caption("Choose Groq (online API) or Ollama (local model).")

# Select chatbot model
model_type = st.sidebar.selectbox(
    "Choose model",
    ["Groq", "Ollama"]
)

ollama_model = st.sidebar.text_input(
    "Ollama model name",
    value="llama3",
    help="Download it first using: ollama pull llama3"
)

if model_type == "Groq":
    st.sidebar.info("Requires a valid GROQ_API_KEY in your .env file.")
else:
    st.sidebar.info("Requires Ollama and a downloaded local model.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear conversation
if st.sidebar.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Ask me anything...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Choose model
                if model_type == "Groq":
                    if not os.getenv("GROQ_API_KEY"):
                        raise ValueError(
                            "Groq API key missing. Add GROQ_API_KEY "
                            "to your .env file."
                        )

                    model = ChatGroq(
                        model="openai/gpt-oss-120b",
                        temperature=0.3
                    )

                else:
                    model = ChatOllama(
                        model=ollama_model,
                        temperature=0.3
                    )

                # Prepare conversation prompt
                prompt_messages = [
                    (
                        "system",
                        "You are a helpful Q&A chatbot. "
                        "Answer clearly, simply, and conversationally."
                    )
                ]

                for msg in st.session_state.messages[:-1]:
                    role = (
                        "human"
                        if msg["role"] == "user"
                        else "ai"
                    )
                    prompt_messages.append(
                        (role, msg["content"])
                    )

                prompt_messages.append(("human", "{question}"))

                prompt = ChatPromptTemplate.from_messages(
                    prompt_messages
                )

                chain = prompt | model

                answer = chain.invoke(
                    {"question": question}
                ).content

                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as exc:
                st.error(f"Could not get an answer: {exc}")
