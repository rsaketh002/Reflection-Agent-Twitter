# 🧠 Reflection-Agent: AI Tweet Generator with Self-Critique Loop

This project implements a **LangGraph-powered AI Agent** designed to write high-quality Twitter posts with iterative self-reflection. The agent generates an initial tweet and continuously reflects on its output to improve it until it reaches a satisfactory level.

## ✨ Features

* **LangGraph-based flow**: Uses a cyclic graph between `generate` and `reflect` nodes.
* **Role Reversal Mechanism**: Simulates self-reflection by swapping AI ↔ Human roles during critique.
* **Custom Chains**:
  * `generation_chain`: Crafts high-quality Twitter posts based on user requests or critiques.
  * `reflection_chain`: Critiques the AI’s output to guide the next tweet iteration.

## 🔧 Requirements

- Python 3.11+
- OpenAI API key
- langchain API key
- `langchain`, `langgraph`, `langchain-openai`, `python-dotenv`

## 📦 Installation

```bash
git clone https://github.com/rsaketh002/reflection-agent.git
cd reflection-agent
pip install -r requirements.txt
```

Make sure to add your OpenAI credentials to a `.env` file:

```
OPENAI_API_KEY=your-key-here
LANGCHAIN_API_KEY=your-key-here
```

## 🚀 Usage

Run the main script:

```bash
python main.py
```

Example output:
```
Running the agent...
Here's a tweet about the latest AI trends...
```

## 🧱 Project Structure

```
.
├── main.py               # LangGraph implementation of generate-reflect loop
├── chains.py             # Prompt templates and chain definitions
├── .env                  # Environment variables (OpenAI key, optional LangChain settings)
└── README.md             # You're reading it!
```

## 🧠 How It Works

1. **User Message**: "I want to write a tweet about the latest AI trends."
2. **Generation Node**: The agent writes a first draft.
3. **Reflection Node**: The agent becomes a human critic, reviewing the tweet.
4. **Loop**: The critique is used to regenerate the tweet. This continues until the graph decides to end.

## 🛠 Environment Settings

Set these in your `.env` file:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_PROJECT=Reflection-Agent
```

## 🧪 Example Prompts

Try:
- "Write a tweet about GPT-4."
- "Make a viral tweet about AI in healthcare."
- "Critique this tweet: 'AI is taking over.'"

## 📜 License

MIT License

## 🤝 Contributing

Feel free to open issues or submit PRs to improve the prompts, reflection loop, or LangGraph structure.

---

Built with ❤️ using [LangGraph](https://www.langchain.com/langgraph) and [LangChain](https://www.langchain.com).
```

Let me know if you want the badge section or deployment instructions (e.g., Streamlit or Hugging Face Space).
