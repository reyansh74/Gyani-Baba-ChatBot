# Gyani Baba - Q&A Chatbot

## Overview
This is a Streamlit-based chatbot application that uses LangChain and Google Gemini AI to answer user questions. The app is called "Gyani Baba" and provides an interactive Q&A interface.

## Project Architecture
- **Framework**: Streamlit
- **AI Integration**: Google Gemini (via langchain_google_genai)
- **Language**: Python 3.11
- **Port**: 5000 (frontend)

## Dependencies
- langchain
- langchain_community
- langchain_core
- langchain_google_genai
- streamlit
- python-dotenv
- ipykernel

## Configuration
- Streamlit is configured to run on 0.0.0.0:5000
- CORS and XSRF protection are disabled for Replit proxy compatibility
- The app requires a Google Gemini API key to function

## How It Works
1. User enters their Google Gemini API key in the sidebar
2. User can adjust temperature and max tokens via sliders
3. User types a question in the text area
4. The app uses LangChain to process the question through Google Gemini
5. Response is displayed to the user

## Recent Changes
- 2025-09-30: Initial setup for Replit environment
  - Added langchain_google_genai to requirements.txt
  - Created Streamlit config to allow all hosts and bind to 0.0.0.0:5000
  - Updated .gitignore with Python-specific patterns
  - Configured workflow for the Streamlit app
  - Fixed LangChain API key handling to prevent None assignment errors
  - Changed AI model from gemini-1.5-flash to gemini-1.5-pro
