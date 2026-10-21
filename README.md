# Idea-Up 🚀

**Turn real-world problems into startup ideas and actionable MVP plans using AI.**

Idea-Up is a lightweight AI-powered application built with **LangChain, Ollama, and Streamlit**. It helps users transform a problem statement into a startup concept, essential product features, and a realistic development roadmap.

## ✨ Features

- **Startup Idea Generation:** Generates a startup name, problem-solution statement, target users, and unique value proposition.
- **Feature Planning:** Suggests essential MVP features and potential future enhancements.
- **MVP Roadmap:** Creates a practical development plan designed around a one-week timeline.
- **Local LLM Inference:** Uses Ollama to run the language model locally.

## 🛠️ Tech Stack

- Python
- Streamlit — user interface
- LangChain — prompt templates and sequential chains
- Ollama — local language model runtime
- Qwen 2.5 3B — language model

## ⚙️ How It Works

1. The user enters a real-world problem.
2. LangChain generates a startup idea.
3. The idea is passed to the next chain to generate product features.
4. The final chain uses the idea and features to create an MVP development plan.
5. Streamlit displays the generated startup blueprint.

## 📁 Project Structure

```text
Idea-Up/
├── app.py
├── chains.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- Git
- [Ollama](https://ollama.com/) installed

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Idea-Up.git
cd Idea-Up
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download the model

```bash
ollama pull qwen2.5:3b
```

Ensure Ollama is running before launching the application.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal.

## 🎯 Project Goals

- Explore LangChain Expression Language (LCEL).
- Build a multi-stage LLM workflow.
- Experiment with local language models.
- Generate structured, practical startup planning suggestions.

## 🔮 Future Improvements

- Structured output validation using Pydantic.
- Better input validation and error handling.
- Export generated plans as Markdown or PDF.
- Idea feasibility scoring and conditional workflows.

## 👩‍💻 Author

**Preethi Sanjay**

Built as a learning project to explore local LLMs, LangChain, and AI application development.
