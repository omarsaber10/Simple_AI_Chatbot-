# Simple_AI_Chatbot

A smart conversational AI powered by **Llama 3.3-70b** (via Groq API), wrapped in a custom  built with Streamlit. Fast. Intelligent. Dark.

---

## 🌟 Features

- 🧠 **Context-Aware Responses** — Maintains full conversation context for coherent multi-turn dialogue
- 💬 **Session-Based Chat History** — Remembers everything you've said within a session
- 🎨 **Dark Knight UI** — Custom CSS with a sleek Gotham-inspired dark theme
- ⚡ **Lightning-Fast Inference** — Powered by Groq's ultra-low-latency API with `llama-3.3-70b-versatile`
- 🔗 **LangChain Integration** — Robust prompt chaining with `ChatPromptTemplate` and `StrOutputParser`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.9+ |
| **UI Framework** | [Streamlit](https://streamlit.io/) |
| **LLM Orchestration** | [LangChain](https://www.langchain.com/) |
| **Inference Provider** | [Groq Cloud API](https://console.groq.com/) |
| **Model** | `llama-3.3-70b-versatile` |
| **Environment Config** | `python-dotenv` |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** — [Download here](https://www.python.org/downloads/)
- **pip** — Comes bundled with Python
- A free **Groq API Key** — [Get yours here](https://console.groq.com/keys)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-batman-chat-assistant.git
cd ai-batman-chat-assistant
```

### 2. Create a Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install streamlit langchain-groq python-dotenv
```

Or install from the requirements file (if provided):

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root of your project:

```bash
touch .env
```

Add your Groq API key inside `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Usage

Start the Streamlit app with a single command:

```bash
streamlit run app.py
```

Your browser will automatically open at `http://localhost:8501`. Type your message, hit **Send**, and the Dark Knight will respond.

---

## 📁 Project Structure

```
ai-batman-chat-assistant/
│
├── app.py              # Main application file
├── .env                # Environment variables (⚠️ never commit this!)
├── .gitignore          # Git ignore file
└── README.md           # You are here
```

---

## ⚠️ Security Note

> **Never upload your `.env` file to GitHub or any public repository.**

Your `.env` file contains your secret API key. Exposing it publicly can lead to unauthorized usage and unexpected charges on your Groq account.

Make sure your `.gitignore` file includes the following:

```gitignore
.env
__pycache__/
*.pyc
venv/
```

---

## 🗺️ Roadmap

- [ ] 🌐 Deploy to Streamlit Community Cloud
- [ ] 🧩 Add support for multiple LLM providers (OpenAI, Gemini)
- [ ] 📂 Export chat history to `.txt` or `.pdf`
- [ ] 🔐 Add user authentication
- [ ] 🎭 Add selectable personas (not just Batman!)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Groq](https://groq.com/) for blazing-fast LLM inference
- [LangChain](https://www.langchain.com/) for seamless LLM chaining
- [Streamlit](https://streamlit.io/) for the rapid UI framework
- The Dark Knight himself, for the inspiration 🦇

---
