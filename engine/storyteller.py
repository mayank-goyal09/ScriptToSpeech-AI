import os
import sys
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

class StoryTeller:
    def __init__(self):
        # We will use Hugging Face's 100% Free Serverless Inference as the primary engine
        # since it runs perfectly on Hugging Face Spaces and locally without rate limits or costs!
        self.use_hf = True
        
        # We use Qwen 2.5 72B Instruct - one of the best and fastest open-source models in the world!
        try:
            self.client = InferenceClient(
                model="Qwen/Qwen2.5-72B-Instruct",
                token=HF_TOKEN
            )
            print("Connected to Hugging Face Free Serverless Inference API (Model: Qwen2.5-72B)")
        except Exception as e:
            print(f"HF Inference Init failed: {e}. Trying Gemini fallback.")
            self.use_hf = False
            
        # Initialize Gemini as a robust backup/fallback
        self.gemini_available = False
        if GOOGLE_API_KEY:
            try:
                genai.configure(api_key=GOOGLE_API_KEY)
                self.model = genai.GenerativeModel('gemini-2.0-flash')
                self.gemini_available = True
                print("Gemini API Backup Initialized (Model: gemini-2.0-flash)")
            except Exception as e:
                print(f"Gemini API Init failed: {e}")

        # If neither is available, raise an error
        if not self.use_hf and not self.gemini_available:
            raise ValueError("No storyteller backend could be initialized. Please check your network or API Keys.")

    def generate_story(self, keywords, genre):
        prompt = f"Write a creative {genre} short story (max 100 words) based on these keywords: {keywords}. Keep it engaging, vivid, and concise. Do not include any title or introduction, start directly with the story."
        
        if self.use_hf:
            try:
                messages = [
                    {"role": "system", "content": "You are a creative writer who writes highly engaging, immersive short stories under 100 words."},
                    {"role": "user", "content": prompt}
                ]
                response = self.client.chat_completion(
                    messages=messages,
                    max_tokens=200
                )
                story_content = response.choices[0].message.content.strip()
                if story_content:
                    return story_content
                raise ValueError("Empty response received from HF model")
            except Exception as e:
                print(f"[WARNING] HF Generation failed: {e}. Trying Gemini fallback...")
                last_error = f"HF Error: {str(e)}"
                
        # Gemini Fallback / Primary if HF disabled
        if self.gemini_available:
            try:
                response = self.model.generate_content(prompt)
                return response.text.strip()
            except Exception as e:
                return f"Error generating story: {e}"
        else:
            return f"Error: Generation failed.\n\nDetail: {last_error}\n\n(No Gemini API Key was found as a fallback)"