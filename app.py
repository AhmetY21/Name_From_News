import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from utils import journalist_response

# Load environment variables (API key)
def get_api_key():
    try:
        # Try to get the API key from Streamlit secrets
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            return api_key
    except KeyError:
        # If that fails, try to get the API key from environment variables
        api_key = st.secrets["OPENAI_API_KEY"]
        if api_key:
            return api_key
        else:
            # If no valid API key is found, raise an error
            raise ValueError("API key not found in Streamlit secrets or environment variables.")

# Get the API key
try:
    api_key = get_api_key()
    # Initialize the OpenAI API client by setting the API key in the configuration
    client = OpenAI(api_key=api_key) # Note: OpenAI client expects 'api_key' to be set like this
except ValueError as e:
    st.error(f"Error: {e}")

# Streamlit App
st.markdown("<h1 style='text-align: center; color: darkblue; font-size: 3em;'>✨ Extract Names from News ✨</h1>", unsafe_allow_html=True)

# Input text box for the article
news_text = st.text_area("Enter the news article text below:", height=200)

# Button to extract names
if st.button("Extract Names"):
    if news_text:
        try:
            # Call the journalist_response function to get the list of names
            names = journalist_response(news_text)
            if names:
                st.text_area("List of People Found:", names, height=100)
            else:
                st.text_area("List of People Found:", "No names found.", height=100)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please provide some text to extract names from.")
