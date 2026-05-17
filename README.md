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

Voice Story Engine is a high-performance AI application that generates creative short stories based on your keywords and narrates them using ultra-realistic neural voices. It features a smart **Dual-Engine Hybrid Architecture** designed to run 100% free with high rate limits on Hugging Face Spaces using serverless LLMs, while providing seamless local developer fallback to Google Gemini.

---

## 🚀 Features

- **Dual-Engine Storyteller**: Uses Hugging Face's Free Serverless Inference (`Qwen 2.5 72B`) on remote deployments to avoid IP rate-limiting, and automatically falls back to **Gemini 2.0 Flash** for local development.
- **Ultra-Realistic Narration**: Uses Microsoft's Edge TTS technology for high-quality, human-like voice synthesis with custom isolated thread-safe loops.
- **Customizable Experience**: Choose from multiple genres (Sci-Fi, Horror, Fantasy, etc.) and a variety of global neural voices.
- **Stunning UI**: Features a custom-built, animated "Fire" theme with glassmorphism aesthetics.
- **Zero-GPU Required**: Runs efficiently on standard CPUs, making it accessible to everyone.

## 🛠️ Tech Stack

- **Core**: Python 3.13
- **Primary AI Engine (Spaces)**: Qwen 2.5 72B Instruct via HF Serverless Inference Client
- **Local Fallback Engine**: Google Gemini 2.0 Flash (`google-generativeai`)
- **Voice Synthesis**: Edge TTS (Microsoft Neural)
- **Framework**: Gradio 5.29.0
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

3. **Configure Environment Keys**:
   * **For Local Execution (Gemini Fallback)**:
     Create a `.env` file in the root directory and add your Google Gemini API Key:
     ```env
     GOOGLE_API_KEY=your_actual_api_key_here
     ```
   * **For Remote Deployments (Hugging Face Spaces)**:
     Add a repository secret named `HF_TOKEN` under your Space's Settings page. This gives the app a dedicated, zero-cost quota to query Hugging Face's high-performance serverless endpoints without encountering shared IP rate blocks.

## 🎮 Usage

Launch the application by running:
```bash
python app.py
```
Open the provided local URL (default: `http://127.0.0.1:7860`) in your browser to start creating!

---

## 📂 Project Structure

- `app.py`: Main Gradio interface, responsive glassmorphic styles, and thread-safe async callbacks.
- `engine/`:
  - `storyteller.py`: Hybrid client checking for `HF_TOKEN` and querying serverless LLMs with standard Gemini fallback.
  - `narrator.py`: Multi-threaded asynchronous worker for generating Edge TTS audio safely inside active event loops.
- `.env`: (Ignored) Stores your private API keys.
- `requirements.txt`: List of necessary Python packages.

---

Built with ❤️ by [Mayank Goyal](https://github.com/mayank-goyal09)
