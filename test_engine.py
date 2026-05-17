from engine.storyteller import StoryTeller
from engine.narrator import Narrator
import os

def run_test():
    print("🚀 Initializing the Story Engine Test...")

    # 1. Initialize StoryTeller 
    try:
        story_teller = StoryTeller()
    except Exception as e:
        print(f"❌ Error initializing StoryTeller: {e}")
        return

    # 2. Generate a Story
    keywords = "haunted spaceship, ghost in the machine, quiet hum"
    genre = "Science Fiction Horror"
    
    print("\n📝 Generating Story with Gemini API...")
    story_text = story_teller.generate_story(keywords, genre)
    
    print("-" * 50)
    print(f"STORY OUTPUT:\n{story_text}")
    print("-" * 50)

    # 3. Narrate the Story with Edge TTS
    print("\n🎤 Narrating Story with Edge TTS (High Quality)...")
    narrator = Narrator()
    
    # Using a cool sci-fi voice (ChristopherNeural is deep/calm)
    audio_file = narrator.generate_audio_file(story_text, voice="en-US-ChristopherNeural")
    
    if audio_file and os.path.exists(audio_file):
        print(f"\n✅ SUCCESS! Audio saved to: {audio_file}")
        # Play it!
        os.system(f"start {audio_file}")
    else:
        print("\n❌ Failed to generate audio.")

if __name__ == "__main__":
    run_test()