import streamlit as st
from openai import OpenAI
import datetime
import os
from dotenv import load_dotenv
import os

# Load environment variables from .env file
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
    client = OpenAI(api_key=api_key)  # Note: OpenAI client expects 'api_key' to be set like this
except ValueError as e:
    st.error(f"Error: {e}")

def journalist_response(news_text):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                "role": "system",
                "content": ("You are a journalist specializing in identifying people mentioned in articles. "
                            "Read the provided article and extract the full names of people explicitly mentioned. "
                            "ONLY provide the list of proper names of people (first and last names). "
                            "Do NOT include names of organizations, places, or objects. "
                            "Provide the list of names in a clean, comma-separated format. "
                            "For example, if the article mentions 'Elon Musk and Steve Jobs', your response should be: 'Elon Musk, Steve Jobs'.")
            },
            {
                "role": "user",
                "content": news_text
            }
        ]
    )

    list_of_people = response.choices[0].message.content.strip()  # Ensures clean format
    
    return list_of_people
