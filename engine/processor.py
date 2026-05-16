from pydub import AudioSegment
import os

class AudioProcessor:
    def __init__(self):
        self.music_path = "assets/background_music/"

    def mix_audio(self, narration_path, theme="sci-fi", output_filename="final_story.mp3"):
        # 1. Load the AI Narration
        narration = AudioSegment.from_wav(narration_path)
        
        # 2. Select background music based on theme
        # Make sure you have 'sci-fi.mp3' in your assets/background_music/ folder!
        bg_music_file = os.path.join(self.music_path, f"{theme}.mp3")
        
        if os.path.exists(bg_music_file):
            bg_music = AudioSegment.from_file(bg_music_file)
            
            # 3. Adjust Volume (Lower music by 20 decibels)
            bg_music = bg_music - 20 
            
            # 4. Loop music if it's shorter than the story
            if len(bg_music) < len(narration):
                bg_music = bg_music * (len(narration) // len(bg_music) + 1)
            
            # 5. Trim music to match narration exactly
            bg_music = bg_music[:len(narration)]
            
            # 6. The "Overlay" (Mixing)
            final_mix = bg_music.overlay(narration)
        else:
            print(f"⚠️ Theme music for {theme} not found. Using raw narration.")
            final_mix = narration

        # 7. Final Export
        final_path = os.path.join("output", output_filename)
        final_mix.export(final_path, format="mp3")
        
        return final_path