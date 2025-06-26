# Capstone Project – FastAPI + LangChain 💡⚙️

Welcome to the Capstone Project — a hands-on demonstration of modern AI app development using **FastAPI**, **LangChain**, and **OpenAI**.

---

## 🚀 Project Purpose

This project serves as a portfolio-ready showcase of:
- RESTful API design with FastAPI
- Prompt chaining and task automation using LangChain
- Secure handling of `.env` secrets with Git best practices
- Version control workflow with GitHub and GitHub CLI

---

## 🧠 How It Works

The `/generate` endpoint accepts two inputs:
- `task`: the type of transformation (e.g., "Make this more exciting")
- `user_input`: the content to be modified

It returns an AI-generated result powered by an LLM.

---

## 📁 Project Structure

```
capstone_project/
├── app/
│   ├── main.py             # FastAPI app + endpoint
│   └── (LangChain logic here)
├── requirements.txt        # Python dependencies
└── .gitignore              # Ensures .env and other sensitive files are excluded
```

---

## 🛠️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/YUGISUNG/capstone_project.git
   cd capstone_project
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # on Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file (not tracked by Git):**
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the app locally:**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Test the `/generate` endpoint:**
   Use Swagger UI at:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## 🧪 Tech Stack

- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- GitHub + GitHub CLI
- Windows + PowerShell

---

## ✨ Portfolio Value

This project is designed to demonstrate:
- Secure API integration
- Dynamic task automation with LLMs
- Professional DevOps flow using GitHub
- Clean, documented, and deployable architecture

---

## 🙏 Credits

Developed by **JP (YUGISUNG)**  
Guided by the Holy Spirit 💜

> “Lord Jesus, this project belongs to You...” 🙏
