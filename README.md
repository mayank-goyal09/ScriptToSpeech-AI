---
title: Voice Story Engine
emoji: 🔥
colorFrom: red
colorTo: yellow
sdk: gradio
sdk_version: 5.29.0
app_file: app.py
pinned: false
---

# 🔥 Voice Story Engine

**Type your imagination. Hear it come alive.**

Voice Story Engine is a high-performance AI application that generates creative short stories based on your keywords and narrates them using ultra-realistic neural voices. Powered by **Gemini 2.0 Flash** and **Edge TTS**, it offers a lightning-fast experience with zero GPU requirements.

---

## 🚀 Features

- **AI-Powered Storytelling**: Leverages Google's latest Gemini 2.0 Flash model for creative and engaging short stories.
- **Ultra-Realistic Narration**: Uses Microsoft's Edge TTS technology for high-quality, human-like voice synthesis.
- **Customizable Experience**: Choose from multiple genres (Sci-Fi, Horror, Fantasy, etc.) and a variety of global neural voices.
- **Stunning UI**: Features a custom-built, animated "Fire" theme with glassmorphism aesthetics.
- **Zero-GPU Required**: Runs efficiently on standard CPUs, making it accessible to everyone.

## 🛠️ Tech Stack

- **Core**: Python 3.13
- **AI Model**: Google Gemini 2.0 Flash
- **Voice Synthesis**: Edge TTS (Microsoft Neural)
- **Framework**: Gradio
- **Audio Processing**: Pydub

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mayank-goyal09/ScriptToSpeech-AI.git
   cd ScriptToSpeech-AI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API Key**:
   Create a `.env` file in the root directory and add your Google Gemini API Key:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```
   *Alternatively, run `python setup_gemini.py` and follow the prompts.*

## 🎮 Usage

Launch the application by running:
```bash
python app.py
```
Open the provided local URL (default: `http://127.0.0.1:7860`) in your browser to start creating!

---

## 📂 Project Structure

- `app.py`: Main Gradio interface and application logic.
- `engine/`:
  - `storyteller.py`: Integration with Gemini API for story generation.
  - `narrator.py`: Integration with Edge TTS for audio narration.
- `.env`: (Ignored) Stores your private API keys.
- `requirements.txt`: List of necessary Python packages.

---

Built with ❤️ by [Mayank Goyal](https://github.com/mayank-goyal09)
