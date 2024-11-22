"""
constants.py
"""

import os

from pathlib import Path

# Key constants
APP_TITLE = "Motion G Toolkit Test"
CHARACTER_LIMIT = 100_000

# Gradio-related constants
GRADIO_CACHE_DIR = "./gradio_cached_examples/tmp/"
GRADIO_CLEAR_CACHE_OLDER_THAN = 1 * 24 * 60 * 60  # 1 day

# Error messages-related constants
ERROR_MESSAGE_NO_INPUT = "Please provide at least one PDF file or a URL."
ERROR_MESSAGE_NOT_PDF = "The provided file is not a PDF. Please upload only PDF files."
ERROR_MESSAGE_NOT_SUPPORTED_IN_MELO_TTS = "The selected language is not supported without advanced audio generation. Please enable advanced audio generation or choose a supported language."
ERROR_MESSAGE_READING_PDF = "Error reading the PDF file"
ERROR_MESSAGE_TOO_LONG = "The total content is too long. Please ensure the combined text from PDFs and URL is fewer than {CHARACTER_LIMIT} characters."

# Fireworks API-related constants
FIREWORKS_API_KEY = "xxxxxxxxxx"#os.getenv("FIREWORKS_API_KEY")
FIREWORKS_MAX_TOKENS = 16_384
FIREWORKS_MODEL_ID = "accounts/fireworks/models/llama-v3p1-405b-instruct"
FIREWORKS_TEMPERATURE = 0.1

# OpenAI API-related constants
OPENAI_API_KEY = "X9yQ4V2pJtM7vRg6Lk1WaN5f3ZcB8uT"
OPENAI_BASE_URL = "http://10.4.32.15:5000/api/openai/ve/v1"
OPENAI_MODEL_ID = "gpt-4o-mini"
OPENAI_TEMPERATURE = 0.1

# MeloTTS
MELO_API_NAME = "/synthesize"
MELO_TTS_SPACES_ID = "mrfakename/MeloTTS"
MELO_RETRY_ATTEMPTS = 3
MELO_RETRY_DELAY = 5  # in seconds

MELO_TTS_LANGUAGE_MAPPING = {
    "en": "EN",
    "es": "ES",
    "fr": "FR",
    "zh": "ZJ",
    "ja": "JP",
    "ko": "KR",
}


# Suno related constants
SUNO_LANGUAGE_MAPPING = {
    "English": "en",
    "Chinese": "zh",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Polish": "pl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Spanish": "es",
    "Turkish": "tr",
}

# General audio-related constants
NOT_SUPPORTED_IN_MELO_TTS = list(
    set(SUNO_LANGUAGE_MAPPING.values()) - set(MELO_TTS_LANGUAGE_MAPPING.keys())
)
NOT_SUPPORTED_IN_MELO_TTS = [
    key for key, id in SUNO_LANGUAGE_MAPPING.items() if id in NOT_SUPPORTED_IN_MELO_TTS
]

# Jina Reader-related constants
JINA_READER_URL = "https://r.jina.ai/"
JINA_RETRY_ATTEMPTS = 3
JINA_RETRY_DELAY = 5  # in seconds

# UI-related constants

#- [Llama 3.1 405B 🦙](https://huggingface.co/meta-llama/Llama-3.1-405B) via [Fireworks AI 🎆](https://fireworks.ai/) and [Instructor 📐](https://github.com/instructor-ai/instructor) 

# UI_DESCRIPTION = """
# Generate Podcasts from PDFs using open-source AI.

# Built with:
# - [GPT-4o Mini 🤖](https://huggingface.co/openai/gpt-4o-mini) via [OpenAI 🌐](https://openai.com/)
# - [MeloTTS 🐚](https://huggingface.co/myshell-ai/MeloTTS-English)
# - [Bark 🐶](https://huggingface.co/suno/bark)
# - [Jina Reader 🔍](https://jina.ai/reader/)

# **Note:** Only the text is processed (100k character limits).
# """
UI_DESCRIPTION = """
<div style="position: relative; padding-top: 20px; padding-bottom: 38px; color: white; background: url('https://coolbackgrounds.io/images/backgrounds/index/sea-edge-79ab30e2.png') no-repeat center center; background-size: cover; border-radius: 10px;">
    <h1 style="text-align: center; font-size: 3rem; color: white;">Open NotebookLM</h1>
    <h2 style="text-align: center; font-size: 1.5rem; color: white;">Generate Your Podcasts from PDFs or URLs</h2>

</div>

<div style="opacity: 0.8;">

<p style="text-align: center; font-size: 0.9rem; padding-top: 10px;">
    <a href="https://github.com/motiong-io/open-notebooklm-test" target="_blank" style="color: #12c2e9; display: inline-flex; align-items: center;">Project</a>
    built with
    <a href="https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/" target="_blank" style="color: #12c2e9;">GPT-4o Mini</a>, 
    <a href="https://huggingface.co/myshell-ai/MeloTTS-English" target="_blank" style="color: #12c2e9;">MeloTTS</a>, 
    <a href="https://huggingface.co/suno/bark" target="_blank" style="color: #12c2e9;">Bark</a>, 
    and 
    <a href="https://jina.ai/reader/" target="_blank" style="color: #12c2e9;">Jina Reader</a>
    <br>
    <strong>Note:</strong> Only the text will be processed, and the input must be less than 100,000 characters.
</p>

</div>
"""


UI_AVAILABLE_LANGUAGES = list(set(SUNO_LANGUAGE_MAPPING.keys()))
UI_INPUTS = {
    "file_upload": {
        "label": "1. 📄 Upload your PDF(s)",
        "file_types": [".pdf"],
        "file_count": "multiple",
    },
    "url": {
        "label": "2. 🔗 Paste a URL (optional)",
        "placeholder": "Enter a URL to include its content",
    },
    "question": {
        "label": "3. 🤔 Do you have a specific question or topic in mind?",
        "placeholder": "Enter a question or topic",
    },
    "tone": {
        "label": "4. 🎭 Choose the tone",
        "choices": ["Fun", "Formal"],
        "value": "Fun",
    },
    "length": {
        "label": "5. ⏱️ Choose the length",
        "choices": ["Short (1-2 min)", "Medium (3-5 min)"],
        "value": "Medium (3-5 min)",
    },
    "language": {
        "label": "6. 🌐 Choose the language",
        "choices": UI_AVAILABLE_LANGUAGES,
        "value": "English",
    },
    "advanced_audio": {
        "label": "7. 🔄 Use advanced audio generation? (Experimental)",
        "value": True,
    },
}
UI_OUTPUTS = {
    "audio": {"label": "🔊 Podcast", "format": "mp3"},
    "transcript": {
        "label": "📜 Transcript",
    },
}
UI_API_NAME = "generate_podcast"
UI_ALLOW_FLAGGING = "never"
UI_CONCURRENCY_LIMIT = 3
UI_EXAMPLES = [
    [
        [str(Path("examples/MotionG_bolg_1.pdf"))],
        "",
        "Explain this blog to me like I'm 5 years old",
        "Fun",
        "Short (1-2 min)",
        "English",
        True,
    ],
    [
        [],
        "https://www.motiong.ai/company/about-us",
        "Introduce MotionG to me in a fun way",
        "Fun",
        "Short (1-2 min)",
        "English",
        False,
    ],
    [
        [],
        "https://www.motiong.ai/company/news-room/e3d5e3c8-59aa-41ce-98b1-fe7c44165049",
        "Tell me recent news of MotionG to me in a broadcast style",
        "Formal",
        "Short (1-2 min)",
        "English",
        False,
    ]
]
UI_CACHE_EXAMPLES = False
UI_SHOW_API = True

CSS_STYLES = """
footer {
    visibility: hidden;
}
"""