"""
Configuration file for Zox AI
"""

import os
from pathlib import Path

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b-instruct-q4_K_M")

# Voice Configuration
WHISPER_MODEL_SIZE = os.getenv("WHISPER_MODEL_SIZE", "base")  # tiny, base, small, medium, large
VOICE_RATE = int(os.getenv("VOICE_RATE", "150"))  # Words per minute
VOICE_VOLUME = float(os.getenv("VOICE_VOLUME", "0.9"))  # 0.0 to 1.0
VOICE_INDEX = int(os.getenv("VOICE_INDEX", "0"))  # 0 for male, 1 for female

# Recording Configuration
RECORDING_DURATION = int(os.getenv("RECORDING_DURATION", "5"))  # seconds
SAMPLE_RATE = int(os.getenv("SAMPLE_RATE", "16000"))  # Hz

# GUI Configuration
WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", "500"))
WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", "700"))
WINDOW_X = int(os.getenv("WINDOW_X", "100"))
WINDOW_Y = int(os.getenv("WINDOW_Y", "100"))

# Paths
BASE_DIR = Path.home() / "Documents" / "Zox AI"
SCREENSHOT_DIR = Path.home() / "Pictures" / "Zox AI_Screenshots"
LOG_DIR = BASE_DIR / "logs"

# Create directories
BASE_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = LOG_DIR / "zoxai.log"

# Browser Configuration
DEFAULT_BROWSER = os.getenv("DEFAULT_BROWSER", None)  # chrome, firefox, edge, or None for system default

# System Configuration
MAX_RAM_GB = int(os.getenv("MAX_RAM_GB", "7"))  # Maximum RAM usage target

# Feature Flags
ENABLE_VOICE_INPUT = os.getenv("ENABLE_VOICE_INPUT", "true").lower() == "true"
ENABLE_VOICE_OUTPUT = os.getenv("ENABLE_VOICE_OUTPUT", "true").lower() == "true"
ENABLE_SCHEDULER = os.getenv("ENABLE_SCHEDULER", "true").lower() == "true"

# Safety Settings
CONFIRM_DESTRUCTIVE_ACTIONS = os.getenv("CONFIRM_DESTRUCTIVE_ACTIONS", "true").lower() == "true"
ALLOWED_FILE_OPERATIONS = ["create", "read", "write", "delete", "copy", "move"]

# LLM Settings
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.3"))
LLM_TOP_P = float(os.getenv("LLM_TOP_P", "0.9"))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "500"))
LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", "30"))  # seconds
