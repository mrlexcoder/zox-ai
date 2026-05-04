# 🤖 Zox AI - Your Offline AI Desktop Assistant

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![Ollama](https://img.shields.io/badge/Ollama-Llama%203.1%208B-orange.svg)](https://ollama.com)

**A fully offline Windows AI desktop assistant powered by Ollama + Llama 3.1 8B model.**

Built by **[MrLexCoder](https://github.com/mrlexcoder)** 🚀

---

## ✨ Features

- 🎤 **Voice Input** - Offline speech-to-text using faster-whisper
- 🔊 **Voice Output** - Offline text-to-speech using pyttsx3
- 💬 **Modern GUI** - Floating chat interface with PyQt6
- 🖥️ **Full Computer Control** - Apps, files, mouse, keyboard automation
- 🧠 **AI-Powered** - Llama 3.1 8B model via Ollama (localhost:11434)
- 📊 **System Monitoring** - CPU, RAM, disk usage tracking
- 🌐 **Browser Control** - Open URLs, search, navigate
- 📸 **Screenshots** - Capture and save screenshots
- ⏰ **Task Scheduling** - Schedule and automate tasks
- 🎯 **Human-like Input** - Realistic typing with delays

---

## 🚀 Quick Start

### Prerequisites
- Windows 10/11 (64-bit)
- 12GB RAM minimum
- Python 3.9+
- 10GB free disk space

### Installation (5 minutes)

#### Step 1: Install Ollama
```bash
# Download from https://ollama.com
ollama pull llama3.1:8b-instruct-q4_K_M
```

#### Step 2: Install Zox AI
```bash
# Clone the repository
git clone https://github.com/mrlexcoder/zox-ai.git
cd zox-ai

# Install dependencies
pip install -r requirements.txt
```

#### Step 3: Run Zox AI
```bash
python main.py
```

Or use the quick launcher:
```bash
scripts\run.bat
```

---

## 📖 Documentation

- 📘 **[Quick Start Guide](docs/QUICKSTART.md)** - Get started in 5 minutes
- 📗 **[Setup Guide](docs/SETUP_GUIDE.md)** - Detailed installation instructions
- 📙 **[Commands Reference](docs/COMMANDS.md)** - Complete command list
- 📕 **[Project Summary](docs/PROJECT_SUMMARY.md)** - Technical overview
- 📔 **[Checklist](docs/CHECKLIST.md)** - Verification steps
- 📓 **[File Structure](docs/FILE_STRUCTURE.md)** - Project organization

---

## 🎮 Usage

### Voice Commands
- Click "Start Listening" to use voice input
- Type in the chat box for text input
- Zox AI will respond with voice and execute actions

### Example Commands
- "Open Chrome and go to YouTube"
- "Create a file called notes.txt with hello world"
- "Take a screenshot"
- "What's my CPU usage?"
- "Type 'Hello World' with human-like speed"
- "Move mouse to center of screen"
- "Set volume to 50%"

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     ZOX AI ARCHITECTURE                      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Voice Input  │  │  Chat GUI    │  │ Voice Output │     │
│  │ (Whisper)    │  │  (PyQt6)     │  │  (pyttsx3)   │     │
│  └──────┬───────┘  └──────┬───────┘  └──────▲───────┘     │
└─────────┼──────────────────┼──────────────────┼─────────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                        AI BRAIN (LLM)                        │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  Ollama + Llama 3.1 8B (localhost:11434)             │ │
│  │  • Understands natural language                       │ │
│  │  • Generates JSON action plans                        │ │
│  │  • Fully offline, no API keys                         │ │
│  └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      ACTION EXECUTOR                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ App Control  │  │ File Control │  │ Mouse/Keys   │     │
│  │ • Open apps  │  │ • Create     │  │ • Type text  │     │
│  │ • Close apps │  │ • Read       │  │ • Move mouse │     │
│  │ • Focus      │  │ • Delete     │  │ • Click      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Browser      │  │ System       │  │ Scheduler    │     │
│  │ • Open URLs  │  │ • Volume     │  │ • Schedule   │     │
│  │ • Search     │  │ • Brightness │  │ • Recurring  │     │
│  │ • Navigate   │  │ • Screenshot │  │ • Reminders  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      WINDOWS SYSTEM                          │
│  • Applications  • Files  • Mouse  • Keyboard  • Settings   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
zox-ai/
├── 📄 main.py                    # Main application entry point
├── 📄 config.py                  # Configuration settings
├── 📄 test_components.py         # Component testing suite
├── 📄 requirements.txt           # Python dependencies
├── 📄 LICENSE                    # MIT License
├── 📄 README.md                  # This file
│
├── 📁 core/                      # Core functionality
│   ├── llm.py                    # Ollama LLM interface
│   ├── voice_input.py            # Speech-to-text (Whisper)
│   └── voice_output.py           # Text-to-speech (pyttsx3)
│
├── 📁 actions/                   # Action handlers
│   ├── app_control.py            # Application management
│   ├── file_control.py           # File operations
│   ├── mouse_keyboard.py         # Input control
│   ├── browser_control.py        # Browser automation
│   ├── system_control.py         # System control
│   └── scheduler.py              # Task scheduling
│
├── 📁 docs/                      # Documentation
│   ├── QUICKSTART.md             # 5-minute setup guide
│   ├── SETUP_GUIDE.md            # Detailed installation
│   ├── COMMANDS.md               # Command reference
│   ├── PROJECT_SUMMARY.md        # Technical overview
│   ├── CHECKLIST.md              # Verification checklist
│   ├── FILE_STRUCTURE.md         # Project organization
│   └── BUILD_COMPLETE.md         # Build summary
│
└── 📁 scripts/                   # Utility scripts
    ├── install.bat               # Installation script
    └── run.bat                   # Quick launcher
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Voice Input** | faster-whisper | Offline speech-to-text (CPU) |
| **AI Brain** | Ollama + Llama 3.1 8B | Natural language understanding |
| **Voice Output** | pyttsx3 | Offline text-to-speech |
| **GUI** | PyQt6 | Modern chat interface |
| **Automation** | pyautogui | Mouse/keyboard control |
| **System** | psutil, pycaw | System monitoring & control |
| **Browser** | webbrowser | URL opening & navigation |

---

## 🔒 Privacy & Security

- ✅ **100% Offline** - No internet required after setup
- ✅ **No Cloud Services** - Everything runs locally
- ✅ **No API Keys** - No external dependencies
- ✅ **No Data Collection** - Your data stays on your machine
- ✅ **Open Source** - All code is visible and auditable

---

## 📊 Performance

- **RAM Usage**: ~7GB (within 12GB system)
- **Response Time**: 1-3 seconds per command
- **Startup Time**: ~5 seconds (after Ollama warm-up)
- **Model Size**: ~5GB (Llama 3.1 8B Q4)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **[Ollama](https://ollama.com)** - Local LLM runtime
- **[Meta](https://ai.meta.com)** - Llama 3.1 model
- **[OpenAI](https://openai.com)** - Whisper model
- **[PyQt6](https://www.riverbankcomputing.com/software/pyqt/)** - GUI framework
- All open-source contributors

---

## 📞 Support

- 📧 Email: mrlexcder@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/mrlexcoder/zox-ai/issues)
- 📖 Docs: [Documentation](docs/)

---

## ⭐ Star History

If you find Zox AI useful, please consider giving it a star! ⭐

---

**Built with ❤️ by [MrLexCoder](https://github.com/mrlexcoder)**

*Your personal AI assistant, completely offline, completely yours.*
