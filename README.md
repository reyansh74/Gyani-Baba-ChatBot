# Gyani Baba ChatBot

Gyani Baba ChatBot is a simple Streamlit-based AI Q&A assistant built with LangChain and Groq. The app is designed as a lightweight chatbot interface where users can enter a question, provide a Groq API key, and receive a fast AI-generated answer.

## Overview

This project focuses on a clean beginner-friendly chatbot workflow:

- Streamlit for the user interface
- LangChain for prompt orchestration
- Groq for fast LLM inference
- environment-variable support through `python-dotenv`

The current app presents a Hindi-flavored chatbot identity called **Gyani Baba**, making the experience more personal and memorable than a generic Q&A tool.

## Features

- Simple web UI built with Streamlit
- Groq-powered AI responses
- Adjustable temperature and max token controls
- Optional LangSmith tracing support
- Lightweight setup for experimentation and demos

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- python-dotenv

## Project Structure

```text
Gyani-Baba-ChatBot/
|-- app.py
|-- requirements.txt
|-- replit.md
|-- .replit
|-- .gitignore
|-- .streamlit/
`-- .vscode/
```

## How It Works

1. The user opens the Streamlit app.
2. The user enters a Groq API key in the sidebar.
3. The user adjusts temperature and max token settings.
4. The user asks a question in the text area.
5. LangChain sends the prompt to Groq using `llama-3.1-8b-instant`.
6. The answer is displayed in the UI.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/reyansh74/Gyani-Baba-ChatBot.git
cd Gyani-Baba-ChatBot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

## API Key

This app currently uses **Groq**, so you need a Groq API key.

Get one from:
[https://console.groq.com/](https://console.groq.com/)

You can enter it directly in the app sidebar when the app starts.

## Current Model

The app currently uses:

```text
llama-3.1-8b-instant
```

via Groq.

## Notes

- The current chatbot is best described as a **single-turn Q&A assistant**, not a full multi-turn memory chatbot.
- The project branding is stronger than the current system prompt, so future improvements can make the assistant personality more distinctive.
- Some dependencies in `requirements.txt` are broader than what the current app strictly needs.

## Suggested Improvements

- Add chat history with Streamlit session state
- Make the Gyani Baba persona more unique in the prompt
- Clean up unused dependencies
- Improve the UI styling for stronger portfolio presentation
- Add deployment instructions for Streamlit Cloud or Hugging Face Spaces

## Author

**Reyansh Pandey**

- GitHub: [https://github.com/reyansh74](https://github.com/reyansh74)
- LinkedIn: [https://linkedin.com/in/reyansh-pandey](https://linkedin.com/in/reyansh-pandey)
- Email: reyanshpandey7004@gmail.com
