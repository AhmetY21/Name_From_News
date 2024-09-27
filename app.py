import streamlit as st
import os
from dotenv import load_dotenv
import openai 
from utils import journalist_response

# Load environment variables (API key)
load_dotenv()

# Access the OpenAI API key
#api_key = os.getenv("OPENAI_API_KEY")

api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the OpenAI client
openai.api_key = api_key

# Journalist response function for name extraction


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
