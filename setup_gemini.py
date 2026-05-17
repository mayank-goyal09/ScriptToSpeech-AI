import os

print("=====================================================================================================")
print("Please paste your Google Gemini API Key below and press ENTER.")
print("Get your FREE key here: https://aistudio.google.com/app/apikey")
print("=====================================================================================================")

try:
    api_key = input("API Key: ").strip()
    if not api_key:
        print("Error: No key provided.")
    else:
        # Save to a .env file for the app to use
        with open(".env", "w") as f:
            f.write(f"GOOGLE_API_KEY={api_key}\n")
        print("\nSUCCESS: API Key saved to .env file!")
        print("You are ready to run the story engine!")
except Exception as e:
    print(f"\nERROR: Could not save key. Details: {e}")
