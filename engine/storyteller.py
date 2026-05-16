import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

class StoryTeller:
    def __init__(self):
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found. Please run 'python setup_gemini.py' first!")
        
        print(f"DEBUG: API Key loaded (starts with: {GOOGLE_API_KEY[:6]}...)")
        genai.configure(api_key=GOOGLE_API_KEY)
        # Using Gemini 2.0 Flash (Fast & Efficient)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        print("Connected to Gemini API (Model: gemini-2.0-flash)")

    def generate_story(self, keywords, genre):
        prompt = f"Write a creative {genre} short story (max 100 words) based on these keywords: {keywords}. Keep it engaging and concise."
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating story: {e}"