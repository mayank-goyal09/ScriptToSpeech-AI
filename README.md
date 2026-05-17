<div align="center">

# 🎭 LoreWeaver-AI — Cinematic Multimodal Story Engine

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Outfit&weight=700&size=32&duration=3500&pause=1000&color=e65c00&center=true&vCenter=true&width=900&height=50&lines=Type+Your+Imagination.+Hear+It+Come+Alive.+🎭;Multimodal+AI+Orchestration+Engine;Gemini+3.0+Flash+Preview+⚡+Edge+Neural+TTS)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-5.29.0-orange?style=for-the-badge&logo=gradio&logoColor=white)
![Microsoft](https://img.shields.io/badge/Edge_TTS-Neural-0078D7?style=for-the-badge&logo=microsoft&logoColor=white)
![Google](https://img.shields.io/badge/Gemini_3.0-Creative_Brain-blue?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

<br/>

[![🚀 Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-LoreWeaver_AI-e65c00?style=for-the-badge&labelColor=0c1445)](https://huggingface.co/spaces/mayankg09/Voice-Story-Engine)
[![GitHub Stars](https://img.shields.io/github/stars/mayank-goyal09/ScriptToSpeech-AI?style=for-the-badge&color=ffd700)](https://github.com/mayank-goyal09/ScriptToSpeech-AI/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mayank-goyal09/ScriptToSpeech-AI?style=for-the-badge&color=87ceeb)](https://github.com/mayank-goyal09/ScriptToSpeech-AI/network)

<br/>

### **From Keyword Prompting → High-Fidelity Audio Narration in under 2 seconds!** 🎧
### **A Cloud-First AI Orchestration Pipeline designed for Zero-GPU hardware.** ⚡

</div>

---

## ⚡ **THE PIPELINE AT A GLANCE**

<table>
<tr>
<td width="50%">

### 🎭 **What is LoreWeaver-AI?**

**LoreWeaver-AI** is a high-performance, lightweight multimodal AI orchestration pipeline designed to synthesize custom, audio-rich stories instantly on low-compute hardware without heavy local dependencies. 

By decoupling heavy local computations, the system leverages a high-speed cloud-first pipeline to generate creative prose and vocal narrations dynamically in real-time.

**The Complete Pipeline:**
- 🧠 **Creative Core** → Gemini 3.0 Flash Preview generates vivid, sensory-rich scripts.
- 📡 **Serverless Backend** → Serverless LLM endpoints ensure high-frequency, $0-cost API routing.
- 🗣️ **Neural Synthesis** → Edge TTS generates human-like, realistic vocal acting.
- 🎛️ **Audio Engineering** → Thread-isolated event loops compile, stream, and render audio layers instantly.

</td>
<td width="50%">

### ✨ **Key Highlights & Features**

| Feature | Details |
|---------|---------|
| ⚡ **Response Latency** | Under 2.0 seconds end-to-end |
| 💸 **Cost to Run** | 100% Free ($0.00 infrastructure setup) |
| 🗣️ **Vocal Diversity** | Custom neural accents (US, GB, IN, AU) |
| 📚 **Genre Engine** | Adaptive prompts (Sci-Fi, Thriller, Comedy...) |
| 🛡️ **IP-Safe Routing** | Dual-Engine setup to bypass Cloud IP limits |
| 🎨 **UI Theme** | Custom animated Glassmorphism "Fire" UI |
| ⚙️ **Concurrence** | Background multi-threaded task isolation |
| 📱 **Device Support** | Fully responsive (Mobile, Tablet, Desktop) |

</td>
</tr>
</table>

---

## 🛠️ **TECHNOLOGY STACK**

<div align="center">

![Tech Stack](https://skillicons.dev/icons?i=python,github,vscode,html,css)

</div>

| **Category** | **Technologies** | **Purpose** |
|:------------:|:-----------------|:------------|
| 🐍 **Core Language** | Python 3.13 | High-speed orchestrator and scripting backend |
| 🧠 **Primary Brain** | Google Gemini 3.0 Flash | Next-gen contextual scripting and short story generation |
| 🗣️ **Voice Synthesizer** | Microsoft Edge TTS | Ultra-realistic, atmospheric human voice generation |
| 🛡️ **Space LLM Backup** | Qwen 2.5 72B Instruct | Serverless fallback to bypass shared cloud rate limits |
| 🎨 **Web Interface** | Gradio 5.29.0 | Premium Glassmorphic design and reactive components |
| 🎧 **Audio System** | Pydub / ffmpeg | Dynamic audio buffering, sampling, and export |
| 🚀 **Hosting & Remote** | Hugging Face Spaces | Distributed serverless container deployment |

---

## 🔬 **DECOUPLED ARCHITECTURE WORKFLOW**

```mermaid
graph TD
    User([👤 User Keywords + Genre]) --> UI[🎨 Premium Gradio UI]
    UI -->|Trigger| Orchestrator{🐍 Python Orchestrator}
    
    Orchestrator -->|Dynamic Prompt| StoryTeller[🧠 Storyteller Backend]
    StoryTeller -->|1. Try Serverless LLM| Qwen[📡 Qwen 2.5 72B Endpoint]
    StoryTeller -->|2. Try API Key| Gemini[⚡ Gemini 3.0 Flash Preview]
    
    Qwen -->|Return Script| Orchestrator
    Gemini -->|Return Script| Orchestrator
    
    Orchestrator -->|Generate Script Text| UI
    Orchestrator -->|Isolate Async Loop| ThreadPool[⚙️ Background Thread]
    ThreadPool -->|Stream Narration| EdgeTTS[🗣️ Edge Neural Voice Synth]
    
    EdgeTTS -->|High-Fidelity Audio Buffer| Orchestrator
    Orchestrator -->|Render Audio Waveform| UI
    UI --> Player([🎧 Play & Download Story])

    style User fill:#e65c00,color:#fff
    style Orchestrator fill:#1f2937,color:#fff
    style ThreadPool fill:#854d0e,color:#fff
    style Player fill:#16a34a,color:#fff
```

---

## 🚀 **HOW WE COMPLETED IT: CHALLENGES FACED & SOLVED**

### 1. 🛡️ Overcoming Google's Strict Shared Cloud IP Blocks (429 Quota Error)
* **The Problem:** Deployed on Hugging Face, the standard Gemini free tier triggered an immediate `429 Quota Exceeded` block on launch. This was due to Google treating all traffic from Hugging Face's shared outbound server blocks as a single IP address, instantly exhausting the free-tier quota.
* **The Solution:** Engineered a **Dual-Engine Storyteller backend**. On remote servers, it automatically routes queries through a dedicated Hugging Face Serverless client using private token security (leveraging state-of-the-art `Qwen 2.5 72B Instruct`). For local testing, it seamlessly falls back to the high-performance `Gemini 3.0 Flash Preview` key, keeping the entire pipeline completely free ($0) and secure.

### 2. ⚙️ Solving Gradio's Async Loop Concurrency Collisions
* **The Problem:** The `edge-tts` voice engine relies on async-await loops. When running inside Gradio's active asynchronous callback loops, calling standard async builders crashed the app with a fatal `RuntimeError: This event loop is already running`.
* **The Solution:** Engineered a background thread worker in `narrator.py` that spawns a dedicated, isolated thread. This thread instantiates its own isolated `asyncio` event loop to safely generate and stream the speech buffers, preventing concurrency collisions and making generation extremely smooth and resilient.

### 3. 🎚️ Disabling Text Search Overlays on Selector Dropdowns
* **The Problem:** Gradio dropdown components default to being filterable search boxes. This treated voice identifiers like `en-US-AriaNeural` as typing inputs, showing ugly spellcheck underlines and text cursor prompts in the UI.
* **The Solution:** Configured the components with `filterable=False`, transforming them into pure, clean select elements that align with high-end native selection aesthetics.

---

## 📂 **PROJECT STRUCTURE**

```
🎭 LoreWeaver-AI/
│
├── 🎨 app.py               # Main Gradio application, responsive CSS, & callbacks
├── 📦 requirements.txt     # Global project dependencies
├── 📖 README.md            # Highly-styled project documentation
│
└── ⚙️ engine/
    ├── 🧠 storyteller.py    # Dual-Engine client (HF Serverless + Gemini fallback)
    └── 🗣️ narrator.py       # Thread-isolated Edge TTS voice synthesis engine
```

---

## 🚀 **QUICK START GUIDE**

### **Step 1: Clone the Repository** 📥

```bash
git clone https://github.com/mayank-goyal09/ScriptToSpeech-AI.git
cd ScriptToSpeech-AI
```

### **Step 2: Install Project Dependencies** 📦

```bash
pip install -r requirements.txt
```

### **Step 3: Add API Credentials (Optional)** 🔑

Create a `.env` file in the root directory to run locally with your Gemini fallback:
```env
GOOGLE_API_KEY=your_gemini_api_key
```

*Note: For remote deployment (Hugging Face Spaces), add your free access token under Space Settings as a Repository Secret named `HF_TOKEN`.*

### **Step 4: Launch the Engine** 🎭

```bash
python app.py
```
Open `http://127.0.0.1:7860` in your web browser to start creating stories!

---

## 👨‍💻 **CONNECT WITH ME**

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-mayank--goyal09-181717?style=for-the-badge&logo=github)](https://github.com/mayank-goyal09)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mayank_Goyal-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mayank-goyal-4b8756363/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit_Site-e65c00?style=for-the-badge&logo=googlechrome&logoColor=white)](https://mayank-portfolio-delta.vercel.app/)

**Mayank Goyal**  
🎭 AI Orchestration Developer | 🧠 NLP Engineer | 🔊 Conversational AI Builder

---

### 🎭 **Built with AI & ❤️ by Mayank Goyal**

*"Decoupling logic, synthesising imagination."* 🎭🔊

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:e65c00,100:f9d423&height=120&section=footer)

</div>
