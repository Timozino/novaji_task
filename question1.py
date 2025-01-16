import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment variable
API_KEY = os.getenv('API_KEY')

# Ensure API_KEY is found
if not API_KEY:
    raise ValueError("API key is missing. Please set it in the .env file.")

# The API endpoint
API_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Function to send a query to the Google Gemini API
def get_gemini_response(query):
    headers = {
        "Content-Type": "application/json"
    }

    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": query}
                ]
            }
        ]
    }

    # POST request to the Gemini API endpoint
    try:
        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            response_data = response.json()
            return response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No answer found.")
        else:
            return f"Error: {response.status_code}, {response.text}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

# Question to ask the Google Gemini API
query = "Who is Donald Trump?"

# Printing response from the API
response = get_gemini_response(query)
print(f"Answer from Gemini API: {response}")
