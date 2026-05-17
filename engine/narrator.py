import asyncio
import threading
import edge_tts
from pydub import AudioSegment
import os

class Narrator:
    def __init__(self):
        # We can select from many high-quality neural voices
        # e.g., 'en-US-AriaNeural', 'en-GB-SoniaNeural', 'en-US-GuyNeural'
        self.output_file = "output/story.mp3"
        print("Connected to Edge TTS (Ultra-Realistic & Fast!)")

    def generate_audio_file(self, text, voice="en-US-AriaNeural"):
        """Generate speech from text using Edge TTS"""
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        
        # Run async TTS in a separate thread to avoid conflicts
        # with Gradio's own event loop (asyncio.run() crashes otherwise)
        try:
            result = [None]
            def run_in_thread():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    loop.run_until_complete(self._generate_async(text, voice))
                finally:
                    loop.close()
            
            t = threading.Thread(target=run_in_thread)
            t.start()
            t.join()
            return self.output_file
        except Exception as e:
            print(f"Error generating audio: {e}")
            return None

    async def _generate_async(self, text, voice):
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(self.output_file)

if __name__ == "__main__":
    n = Narrator()
    n.generate_audio_file("Hello there! This is a test of the amazing Edge TTS system.", "en-US-ChristopherNeural")
    print("Audio generated successfully!")