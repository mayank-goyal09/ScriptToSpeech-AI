import gradio as gr
from engine.storyteller import StoryTeller
from engine.narrator import Narrator
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Engines
print("[INFO] Starting engine initialization...")
try:
    story_engine = StoryTeller()
    narrator_engine = Narrator()
    print("[SUCCESS] All engines initialized successfully!")
except Exception as e:
    story_engine = None
    narrator_engine = None
    print(f"[ERROR] Error initializing engines: {e}")

def process_story(keywords, genre, voice):
    print(f"[INFO] Processing request: keywords='{keywords}', genre='{genre}', voice='{voice}'")
    try:
        if not story_engine or not narrator_engine:
            return "System Error: Engines not initialized. Check your API Key.", None

        # 1. Generate Story
        print("[INFO] Generating story...")
        story = story_engine.generate_story(keywords, genre)
        
        if "Error generating story" in story:
            print(f"[ERROR] {story}")
            return story, None

        # 2. Generate Audio
        print("[INFO] Generating audio...")
        audio_path = narrator_engine.generate_audio_file(story, voice)
        
        if not audio_path:
            print("[ERROR] Audio generation failed.")
            return story, "Error: Audio narration could not be generated."

        print("[SUCCESS] Processing complete!")
        return story, audio_path
        
    except Exception as e:
        error_msg = f"Unexpected System Error: {str(e)}"
        print(f"[CRITICAL] {error_msg}")
        return error_msg, None

# ============================================================
#  🔥 ANIMATED ORANGE THEME - Custom Built CSS
# ============================================================
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

/* ===== ROOT VARIABLES ===== */
:root {
    --fire-1: #ff6b00;
    --fire-2: #ff8c00;
    --fire-3: #ffa500;
    --fire-4: #ffb733;
    --yellow-light: #fff3c4;
    --yellow-btn: #ffe599;
    --yellow-btn-hover: #ffd966;
    --dark-bg: #1a0a00;
    --dark-card: #2a1200;
    --text-light: #fff5e6;
    --text-muted: #cc9966;
}

/* ===== ANIMATED BACKGROUND ===== */
.gradio-container {
    font-family: 'Outfit', sans-serif !important;
    background: var(--dark-bg) !important;
    min-height: 100vh;
    position: relative;
    overflow-x: hidden;
}
.gradio-container::before {
    content: '';
    position: fixed;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: 
        radial-gradient(circle at 20% 80%, rgba(255,107,0,0.15) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255,165,0,0.1) 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(255,140,0,0.08) 0%, transparent 60%);
    animation: aurora-shift 12s ease-in-out infinite alternate;
    z-index: 0;
    pointer-events: none;
}
@keyframes aurora-shift {
    0%   { transform: translate(0, 0) rotate(0deg); }
    33%  { transform: translate(30px, -20px) rotate(2deg); }
    66%  { transform: translate(-20px, 15px) rotate(-1deg); }
    100% { transform: translate(10px, -10px) rotate(1deg); }
}

/* ===== FLOATING FIRE PARTICLES ===== */
.fire-particles {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.fire-particles span {
    position: absolute;
    bottom: -20px;
    width: 6px;
    height: 6px;
    background: var(--fire-3);
    border-radius: 50%;
    opacity: 0;
    animation: float-up 8s linear infinite;
    box-shadow: 0 0 10px var(--fire-2), 0 0 20px var(--fire-1);
}
.fire-particles span:nth-child(1)  { left: 10%; animation-delay: 0s; animation-duration: 7s; }
.fire-particles span:nth-child(2)  { left: 25%; animation-delay: 1.5s; animation-duration: 9s; width: 4px; height: 4px; }
.fire-particles span:nth-child(3)  { left: 40%; animation-delay: 3s; animation-duration: 6s; }
.fire-particles span:nth-child(4)  { left: 55%; animation-delay: 0.5s; animation-duration: 10s; width: 8px; height: 8px; }
.fire-particles span:nth-child(5)  { left: 70%; animation-delay: 2s; animation-duration: 8s; }
.fire-particles span:nth-child(6)  { left: 85%; animation-delay: 4s; animation-duration: 7s; width: 5px; height: 5px; }
.fire-particles span:nth-child(7)  { left: 15%; animation-delay: 5s; animation-duration: 9s; }
.fire-particles span:nth-child(8)  { left: 50%; animation-delay: 1s; animation-duration: 6.5s; width: 7px; height: 7px; }
.fire-particles span:nth-child(9)  { left: 35%; animation-delay: 3.5s; animation-duration: 8.5s; }
.fire-particles span:nth-child(10) { left: 90%; animation-delay: 2.5s; animation-duration: 7.5s; width: 4px; height: 4px; }

@keyframes float-up {
    0%   { transform: translateY(0) scale(1); opacity: 0; }
    10%  { opacity: 0.8; }
    50%  { opacity: 0.4; }
    100% { transform: translateY(-110vh) scale(0.3); opacity: 0; }
}

/* ===== HERO HEADER ===== */
.hero-header {
    text-align: center;
    padding: 30px 20px 15px;
    position: relative;
    z-index: 1;
}
.hero-header h1 {
    font-family: 'Outfit', sans-serif !important;
    font-size: 3em !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg, #ff6b00, #ffa500, #ffd700, #ff8c00) !important;
    background-size: 300% 300% !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    animation: gradient-flow 4s ease infinite !important;
    margin-bottom: 5px !important;
    letter-spacing: -1px;
    text-shadow: none;
}
@keyframes gradient-flow {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero-subtitle {
    color: var(--text-muted) !important;
    font-size: 1.15em !important;
    font-weight: 300 !important;
    letter-spacing: 1px;
}
.hero-badge {
    display: inline-block;
    background: linear-gradient(135deg, var(--fire-1), var(--fire-3));
    color: var(--dark-bg) !important;
    padding: 5px 16px;
    border-radius: 25px;
    font-size: 0.75em;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 12px;
    animation: badge-glow 2s ease-in-out infinite alternate;
}
@keyframes badge-glow {
    0%   { box-shadow: 0 0 8px rgba(255,107,0,0.4); }
    100% { box-shadow: 0 0 20px rgba(255,165,0,0.7); }
}

/* ===== SECTION HEADERS ===== */
.section-title {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.2em !important;
    margin-bottom: 8px !important;
    padding-bottom: 8px;
    border-bottom: 2px solid rgba(255, 165, 0, 0.2);
}

/* ===== PANELS & CARDS (Glassmorphism) ===== */
.gr-group, .gr-box, .gr-panel,
div[class*="block"], div[class*="panel"] {
    background: rgba(42, 18, 0, 0.6) !important;
    border: 1px solid rgba(255, 165, 0, 0.12) !important;
    border-radius: 18px !important;
    backdrop-filter: blur(14px) !important;
    transition: border-color 0.4s ease, box-shadow 0.4s ease !important;
}
.gr-group:hover, .gr-box:hover {
    border-color: rgba(255, 165, 0, 0.25) !important;
    box-shadow: 0 0 30px rgba(255, 107, 0, 0.08) !important;
}

/* ===== LABELS ===== */
label, .label-wrap span {
    color: var(--fire-3) !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95em !important;
}

/* ===== TEXT INPUTS ===== */
input[type="text"], textarea, .gr-text-input {
    background: rgba(255, 165, 0, 0.06) !important;
    border: 1px solid rgba(255, 140, 0, 0.25) !important;
    border-radius: 14px !important;
    color: var(--text-light) !important;
    font-family: 'Outfit', sans-serif !important;
    transition: all 0.35s ease !important;
}
input[type="text"]:focus, textarea:focus {
    border-color: var(--fire-2) !important;
    box-shadow: 0 0 25px rgba(255, 140, 0, 0.2), inset 0 0 10px rgba(255, 140, 0, 0.05) !important;
    outline: none !important;
}

/* ===== DROPDOWNS ===== */
select, .gr-dropdown, div[data-testid="dropdown"] {
    background: rgba(255, 165, 0, 0.06) !important;
    border: 1px solid rgba(255, 140, 0, 0.25) !important;
    border-radius: 14px !important;
    color: var(--text-light) !important;
    font-family: 'Outfit', sans-serif !important;
}

/* ===== LIGHT YELLOW BUTTONS ===== */
button.primary, button[variant="primary"], .gr-button-primary {
    background: linear-gradient(135deg, var(--yellow-btn) 0%, var(--yellow-btn-hover) 100%) !important;
    border: none !important;
    border-radius: 16px !important;
    color: #3d2200 !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1.15em !important;
    padding: 14px 32px !important;
    letter-spacing: 0.5px;
    cursor: pointer !important;
    transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
    box-shadow: 0 4px 20px rgba(255, 200, 0, 0.3) !important;
    position: relative;
    overflow: hidden;
}
button.primary:hover, button[variant="primary"]:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 8px 35px rgba(255, 200, 0, 0.5) !important;
    background: linear-gradient(135deg, var(--yellow-btn-hover) 0%, var(--fire-3) 100%) !important;
}
button.primary:active, button[variant="primary"]:active {
    transform: translateY(0px) scale(0.98) !important;
}

/* ===== STORY OUTPUT AREA ===== */
.story-output textarea {
    background: rgba(255, 200, 0, 0.04) !important;
    border: 1px solid rgba(255, 165, 0, 0.15) !important;
    border-radius: 16px !important;
    color: var(--text-light) !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 1.05em !important;
    line-height: 1.8 !important;
    letter-spacing: 0.2px;
}

/* ===== AUDIO PLAYER ===== */
audio {
    border-radius: 16px !important;
    width: 100% !important;
    filter: sepia(0.3) saturate(1.5) hue-rotate(-10deg);
}

/* ===== DIVIDER LINE ===== */
.fire-divider {
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--fire-1), var(--fire-3), var(--fire-1), transparent);
    background-size: 200% 100%;
    animation: divider-flow 3s linear infinite;
    border-radius: 2px;
    margin: 10px 0 20px;
}
@keyframes divider-flow {
    0%   { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

/* ===== FOOTER ===== */
.footer-info {
    text-align: center;
    padding: 25px;
    color: var(--text-muted);
    font-size: 0.85em;
    font-weight: 300;
    position: relative;
    z-index: 1;
}

/* ===== CUSTOM SCROLLBAR ===== */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--dark-bg); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--fire-1), var(--fire-3));
    border-radius: 4px;
}

/* ===== PULSE RING ON GENERATE ===== */
@keyframes pulse-ring {
    0%   { box-shadow: 0 0 0 0 rgba(255,200,0,0.5); }
    70%  { box-shadow: 0 0 0 15px rgba(255,200,0,0); }
    100% { box-shadow: 0 0 0 0 rgba(255,200,0,0); }
}
</style>
"""

# ============================================================
#  BUILD INTERFACE
# ============================================================
with gr.Blocks(title="Voice Story Engine") as app:

    # Inject CSS + Fire Particles
    gr.HTML(CUSTOM_CSS)
    gr.HTML("""
    <div class="fire-particles">
        <span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span>
    </div>
    """)

    # Hero Header
    gr.HTML("""
    <div class="hero-header">
        <span class="hero-badge">⚡ Powered by Gemini 2.0 Flash</span>
        <h1>🔥 Voice Story Engine</h1>
        <p class="hero-subtitle">Type your imagination. Hear it come alive.</p>
        <div class="fire-divider"></div>
    </div>
    """)
    
    with gr.Row():
        # LEFT: Controls
        with gr.Column(scale=1):
            gr.HTML("<div class='section-title' style='color:#ffa500;'>🎯 Story Settings</div>")
            
            keywords_input = gr.Textbox(
                label="Keywords / Idea",
                placeholder="e.g. cybernetic cat, neon rain, lost key, ancient temple",
                lines=2
            )
            genre_input = gr.Dropdown(
                choices=["Sci-Fi", "Horror", "Fantasy", "Comedy", "Mystery", "Romance", "Thriller", "Adventure"],
                label="Genre",
                value="Sci-Fi"
            )
            voice_input = gr.Dropdown(
                choices=[
                    "en-US-AriaNeural",
                    "en-US-GuyNeural",
                    "en-GB-SoniaNeural",
                    "en-US-ChristopherNeural",
                    "en-IN-NeerjaNeural",
                    "en-AU-NatashaNeural"
                ],
                label="Voice",
                value="en-US-AriaNeural"
            )
            generate_btn = gr.Button("🔥 Generate Story & Audio", variant="primary")
        
        # RIGHT: Output
        with gr.Column(scale=2):
            gr.HTML("<div class='section-title' style='color:#ffd700;'>📖 Your Story</div>")
            story_output = gr.Textbox(label="Generated Story", lines=10, elem_classes=["story-output"])
            audio_output = gr.Audio(label="🎧 Audio Narration", type="filepath")
    
    # Footer
    gr.HTML("""
    <div class="footer-info">
        🔥 Built with Gemini 2.0 Flash + Edge TTS &bull; Zero GPU Required &bull; Lightning Fast ⚡
    </div>
    """)

    generate_btn.click(
        process_story,
        inputs=[keywords_input, genre_input, voice_input],
        outputs=[story_output, audio_output]
    )

if __name__ == "__main__":
    app.launch()