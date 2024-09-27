import streamlit as st
from openai import OpenAI
import datetime
import os
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")



client = OpenAI(api_key=api_key)

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
