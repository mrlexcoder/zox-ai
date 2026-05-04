# Zox AI Setup Guide - Complete Installation Instructions
**Built by MrLexCoder**

## 📋 Prerequisites

- **Windows 10/11** (64-bit)
- **12GB RAM** minimum (Zox AI uses ~7GB max)
- **Python 3.9+** installed
- **10GB free disk space** (for models and dependencies)
- **Internet connection** (for initial setup only)

---

## 🚀 Quick Start (5 Steps)

### Step 1: Install Python
1. Download Python 3.9+ from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Verify installation:
   ```bash
   python --version
   ```

### Step 2: Install Ollama
1. Download Ollama from [ollama.com](https://ollama.com/download)
2. Install and run Ollama
3. Open a new terminal and pull the model:
   ```bash
   ollama pull llama3.1:8b-instruct-q4_K_M
   ```
4. Start Ollama server (if not auto-started):
   ```bash
   ollama serve
   ```

### Step 3: Install Zox AI Dependencies
Run the installation script:
```bash
install.bat
```

Or manually:
```bash
pip install -r requirements.txt
```

### Step 4: Test Components
```bash
python test_components.py
```

This will verify:
- ✓ All Python packages installed
- ✓ Ollama connection working
- ✓ Voice output functional
- ✓ System controls working

### Step 5: Run Zox AI
```bash
python main.py
```

Or use the batch file:
```bash
run.bat
```

---

## 🎯 Detailed Installation

### Option A: Automatic Installation (Recommended)

1. **Clone or download** this repository
2. **Run** `install.bat`
3. **Follow** the on-screen instructions
4. **Install Ollama** and pull the model (see Step 2 above)
5. **Run** `python test_components.py`
6. **Start Zox AI** with `run.bat`

### Option B: Manual Installation

#### 1. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

#### 2. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 3. Install Ollama
- Download from [ollama.com](https://ollama.com/download)
- Install and start the service
- Pull the model:
  ```bash
  ollama pull llama3.1:8b-instruct-q4_K_M
  ```

#### 4. Configure (Optional)
Copy `.env.example` to `.env` and customize:
```bash
copy .env.example .env
```

Edit `.env` to change settings like:
- Voice speed and volume
- Window size and position
- Model selection
- Feature toggles

---

## 🔧 Troubleshooting

### Problem: "Cannot connect to Ollama"
**Solution:**
1. Make sure Ollama is running: `ollama serve`
2. Check if model is installed: `ollama list`
3. If not, pull it: `ollama pull llama3.1:8b-instruct-q4_K_M`
4. Verify connection: `curl http://localhost:11434/api/tags`

### Problem: "Module not found" errors
**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Problem: Voice input not working
**Solution:**
- faster-whisper requires additional setup
- For quick testing, Zox AI will fall back to text input
- To fix: Install CUDA toolkit for GPU acceleration (optional)

### Problem: Volume/Brightness control not working
**Solution:**
- These features require admin privileges on some systems
- Run as administrator if needed
- Some features may not work on all hardware

### Problem: High RAM usage
**Solution:**
- Use smaller Whisper model: Edit `config.py` → `WHISPER_MODEL_SIZE = "tiny"`
- Close other applications
- Ensure you have at least 12GB RAM

### Problem: PyQt6 GUI not showing
**Solution:**
```bash
pip uninstall PyQt6
pip install PyQt6==6.6.1
```

---

## 📦 What Gets Installed

### Core Dependencies
- **PyQt6** - Modern GUI framework
- **requests** - HTTP communication with Ollama
- **psutil** - System information and monitoring

### Voice & Audio
- **faster-whisper** - Offline speech-to-text (CPU-based)
- **pyttsx3** - Offline text-to-speech
- **sounddevice** - Audio recording
- **pycaw** - Windows volume control

### Automation
- **pyautogui** - Mouse and keyboard control
- **pywinauto** - Windows UI automation
- **schedule** - Task scheduling

### System Control
- **screen-brightness-control** - Display brightness
- **pillow** - Screenshot capability

### AI Model
- **torch** - PyTorch for Whisper model
- **numpy** - Numerical operations

---

## 🎮 Usage Examples

### Voice Commands
- "Open Chrome and go to YouTube"
- "Create a file called notes.txt with hello world"
- "Take a screenshot"
- "What's my CPU usage?"
- "Set volume to 50%"
- "Type 'Hello World' slowly"

### Text Commands
Type in the chat box:
- "Open calculator"
- "Search Google for Python tutorials"
- "Move mouse to center"
- "Press enter key"
- "Close Chrome"

---

## 🔒 Security & Privacy

- ✅ **100% Offline** - No data sent to cloud
- ✅ **Local AI** - Llama 3.1 runs on your machine
- ✅ **No API Keys** - No external services required
- ✅ **Open Source** - All code is visible and auditable

---

## 🎨 Customization

### Change Voice Settings
Edit `config.py`:
```python
VOICE_RATE = 150  # Words per minute (100-200)
VOICE_VOLUME = 0.9  # Volume (0.0-1.0)
VOICE_INDEX = 0  # 0=male, 1=female (if available)
```

### Change Window Appearance
Edit `main.py` GUI styles or modify:
```python
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700
```

### Use Different AI Model
Edit `config.py`:
```python
OLLAMA_MODEL = "mistral:7b"  # or any other Ollama model
```

Then pull the model:
```bash
ollama pull mistral:7b
```

### Add Custom Commands
Edit `core/llm.py` system prompt to add new intents and actions.

---

## 📊 System Requirements Details

### Minimum Requirements
- **CPU**: Intel i5 or AMD Ryzen 5 (4 cores)
- **RAM**: 12GB
- **Storage**: 10GB free
- **OS**: Windows 10 (64-bit)

### Recommended Requirements
- **CPU**: Intel i7 or AMD Ryzen 7 (8 cores)
- **RAM**: 16GB
- **Storage**: 20GB free (SSD preferred)
- **OS**: Windows 11 (64-bit)

### RAM Usage Breakdown
- Llama 3.1 8B Q4: ~5GB
- Whisper Base: ~1GB
- Python + PyQt6: ~500MB
- System overhead: ~500MB
- **Total**: ~7GB

---

## 🆘 Getting Help

### Check Logs
Logs are saved to: `Documents/Zox AI/logs/zoxai.log`

### Run Diagnostics
```bash
python test_components.py
```

### Common Issues
1. **Ollama not responding**: Restart Ollama service
2. **High CPU usage**: Normal during AI processing
3. **Slow responses**: First query is slower (model loading)

---

## 🚀 Performance Tips

1. **Use SSD** for faster model loading
2. **Close background apps** to free RAM
3. **Use smaller Whisper model** (`tiny` or `base`) for faster voice recognition
4. **Disable voice input** if not needed (saves ~1GB RAM)
5. **Keep Ollama running** to avoid startup delays

---

## 📝 Development

### Project Structure
```
zoxai/
├── main.py                 # Entry point + GUI
├── config.py              # Configuration
├── core/
│   ├── llm.py            # Ollama interface
│   ├── voice_input.py    # Speech-to-text
│   └── voice_output.py   # Text-to-speech
├── actions/
│   ├── app_control.py    # App management
│   ├── file_control.py   # File operations
│   ├── mouse_keyboard.py # Input control
│   ├── browser_control.py# Browser automation
│   ├── system_control.py # System settings
│   └── scheduler.py      # Task scheduling
└── test_components.py    # Test suite
```

### Running Tests
```bash
python test_components.py
```

### Adding New Features
1. Add action handler in `actions/` directory
2. Update `core/llm.py` system prompt with new intent
3. Add execution logic in `main.py` `execute_actions()`

---

## 📄 License

This project is open source. Feel free to modify and distribute.

**Built by MrLexCoder** 🚀

---

## 🙏 Credits

- **Ollama** - Local LLM runtime
- **Meta** - Llama 3.1 model
- **OpenAI** - Whisper model
- **PyQt6** - GUI framework
- All open-source contributors

---

## 🔄 Updates

Check for updates at: [Your GitHub Repository]

To update:
```bash
git pull
pip install -r requirements.txt --upgrade
```

---

**Enjoy your personal AI assistant! 🤖**
