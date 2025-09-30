import os
from dotenv import load_dotenv
import streamlit as st

from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Optional LangSmith setup (safe to leave even if unused)
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot"

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that helps people find information."),
    ("user", "{question}")
])

# Function to generate response from Gemini
def generate_response(question, temperature, max_tokens, api_key):
    os.environ["GOOGLE_API_KEY"] = api_key
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=temperature,
        max_tokens=max_tokens,
        google_api_key=api_key
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({"question": question})

# Streamlit UI
st.title("Gyani Baba 🧙‍♂️")
st.write("Gyani Baba se poocho.")

# Sidebar: API key input
api_key = st.sidebar.text_input("Enter your Gemini API key", type="password")

# Sidebar: Sliders
temperature = st.sidebar.slider("Select temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Select max tokens", 50, 1024, 256)

# Input box
user_input = st.text_area("Tumhara sawaal yahan likho...")

# Handle response
if user_input:
    if not api_key:
        st.warning("Please enter your Gemini API key.")
    else:
        with st.spinner("Gyani Baba soch rahe hain..."):
            try:
                response = generate_response(user_input, temperature, max_tokens, api_key)
                st.write("### Gyani Baba ka jawab:")
                st.success(response)
            except Exception as e:
                st.error(f"❌ Error: {e}")
else:
    st.info("👆 Upar apna sawaal likho aur Gyani Baba se poochho.")
