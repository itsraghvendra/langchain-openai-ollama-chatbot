# Assignment 29: Q&A Chatbot (OpenAI & Ollama)

This is a simple, beginner-friendly solution for the assignment. It includes:
- Part 1: OpenAI chatbot using LangChain
- Part 2: Local Ollama chatbot using LangChain
- Part 3: One Streamlit app that switches between OpenAI and Ollama
- Part 4: Comparison and short conceptual answers

## 1. Requirements

Install Python 3.10 or newer. OpenAI mode needs internet, an OpenAI API key, and API billing/credits. Ollama mode needs Ollama installed and a model downloaded. You can use either mode independently.

## 2. Install Python packages

Open a terminal in this folder and run:

```bash
python -m venv .venv
```

Windows:
```bat
.venv\Scripts\activate
```

Then install packages:
```bash
python -m pip install -r requirements.txt
```

## 3. Set up OpenAI

1. Copy `.env.example` and rename the copy to `.env`.
2. Open `.env` and replace `your_openai_api_key_here` with your API key.
3. Keep `.env` private. Never upload it or share your key.

Run the OpenAI command-line chatbot:
```bash
python openai_chatbot.py
```

Test questions (at least five):
1. What is Generative AI?
2. Explain Python in simple words.
3. What is the difference between AI and machine learning?
4. Give me three tips to prepare for an interview.
5. Explain a transformer model simply.

## 4. Set up Ollama (local model)

1. Install Ollama from the official website: https://ollama.com/download
2. Open Command Prompt or the VS Code terminal.
3. Download the model:
```bash
ollama pull llama3
```
4. Test the model:
```bash
ollama run llama3
```
Type a question. Use `/bye` to exit the Ollama prompt.
5. Run the LangChain version:
```bash
python ollama_chatbot.py
```

Ollama mode normally runs on your computer and does not require an OpenAI API key. The first model download needs internet and several GB of disk space.

## 5. Run the combined app

Make sure packages are installed. Then run:
```bash
streamlit run app.py
```
Your browser should open the app. Choose OpenAI or Ollama in the sidebar, type a question, and press Enter. For Ollama, make sure the Ollama app/service is running and the model has been downloaded.

## 6. OpenAI vs Ollama (Task 6)

| Factor | OpenAI | Ollama (local model) |
|---|---|---|
| Response quality | Often strong, especially with capable hosted models; depends on model and task. | Depends on the selected local model and computer resources; smaller models may be less accurate. |
| Latency | Requires internet; speed depends on network and API service. | No internet needed after download; speed depends on hardware and model size. |
| Cost | API usage may be charged by tokens. | No per-token API fee, but uses local hardware/electricity and disk space. |
| Privacy | Prompts are sent to the provider's service. Review provider settings/policies for your use case. | Prompts can stay on your computer when using a local model, subject to your own system setup. |

## 7. Conceptual answers (Task 9)

**1. When to prefer OpenAI models:** Use them when you need strong general performance, easy setup, and do not want to manage model hardware. Internet and API access are required.

**2. When to prefer open-source/local models:** Use them when offline operation, local control, privacy, or avoiding per-request API charges is important, and your computer can run the model.

**3. Trade-offs in production systems:** Hosted APIs are easy to scale and maintain but depend on network/provider availability and may incur usage charges. Local models provide more control but require hardware, setup, monitoring, and model updates.

**4. Cost and scalability:** APIs can scale without buying GPUs, but costs can rise with usage. Local models may be economical at high usage if suitable hardware is already available, but scaling requires more compute resources and operations work.

## 8. Troubleshooting

- **`OPENAI_API_KEY` missing:** Ensure `.env` exists in this folder and contains the key.
- **Authentication or quota error:** Check that the API key is valid and the account has API access/credits.
- **Ollama connection error:** Open/start Ollama, then run `ollama list` and `ollama run llama3`.
- **Model not found:** Run `ollama pull llama3` and make sure the model name in the app matches.
- **Package error:** Activate the virtual environment and run `python -m pip install -r requirements.txt` again.

## 9. Files included

- `openai_chatbot.py` — Part 1
- `ollama_chatbot.py` — Part 2
- `app.py` — Part 3 unified Streamlit app
- `requirements.txt` — Python packages
- `.env.example` — sample environment configuration
- `.gitignore` — prevents accidentally committing secrets
