import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai


# Load environment variables
load_dotenv()  # loading of all the environment variables

# Debug: Print to verify the environment variable is loaded
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the generative model with the API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Function to get response from Gemini model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Page setup using Streamlit
st.set_page_config(page_title="Gemini QNA chatbot", 
                   page_icon=":gemini:", 
                   layout="wide",
                   initial_sidebar_state="expanded")

# Setting up header
st.header("Gemini QNA App")

# Input
question = st.text_input("Enter your question:")

if st.button("Submit your question"):
    response = get_gemini_response(question)
    st.write("**You**:", question)
    st.write("**Gemini**:", response)

