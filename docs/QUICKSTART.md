# Zox AI - 5-Minute Quick Start Guide 🚀

**Get Zox AI running in 5 minutes!**

---

## ⚡ Super Quick Start (For Experienced Users)

```bash
# 1. Install Ollama from ollama.com
ollama pull llama3.1:8b-instruct-q4_K_M

# 2. Install Zox AI
pip install -r requirements.txt

# 3. Run Zox AI
python main.py
```

Done! 🎉

---

## 👶 Beginner-Friendly Guide

### Step 1: Install Python (2 minutes)

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click the big yellow "Download Python" button
3. Run the installer
4. **IMPORTANT**: Check the box "Add Python to PATH"
5. Click "Install Now"

**Test it worked:**
- Open Command Prompt (search "cmd" in Windows)
- Type: `python --version`
- You should see something like "Python 3.11.x"

---

### Step 2: Install Ollama (2 minutes)

1. Go to [ollama.com](https://ollama.com/download)
2. Click "Download for Windows"
3. Run the installer
4. Ollama will start automatically

**Download the AI model:**
- Open Command Prompt
- Type: `ollama pull llama3.1:8b-instruct-q4_K_M`
- Wait for download (about 5GB, takes 2-5 minutes)

---

### Step 3: Install Zox AI (1 minute)

1. Download this Zox AI folder to your computer
2. Open Command Prompt
3. Navigate to the Zox AI folder:
   ```bash
   cd C:\path\to\zoxai
   ```
4. Double-click `install.bat`
   
   OR type:
   ```bash
   pip install -r requirements.txt
   ```

---

### Step 4: Run Zox AI (30 seconds)

**Option A: Easy Way**
- Double-click `run.bat`

**Option B: Command Line**
- Open Command Prompt in Zox AI folder
- Type: `python main.py`

---

## 🎮 Your First Commands

When Zox AI opens, try these:

### Type in the chat box:

1. **"Hello"**
   - Zox AI will greet you

2. **"Open Calculator"**
   - Calculator app will open

3. **"What's my CPU usage?"**
   - Zox AI will show your system stats

4. **"Take a screenshot"**
   - Screenshot saved to Pictures/Zox AI_Screenshots

5. **"Open YouTube"**
   - YouTube opens in your browser

---

## 🎤 Using Voice (Optional)

1. Click the **"🎤 Start Listening"** button
2. Speak your command clearly
3. Wait for Zox AI to respond

**Note**: Voice input requires a microphone and may take longer to set up. Text input works great too!

---

## ❓ Common Issues

### "Cannot connect to Ollama"
**Fix**: 
- Open Command Prompt
- Type: `ollama serve`
- Try running Zox AI again

### "Module not found" error
**Fix**:
- Open Command Prompt in Zox AI folder
- Type: `pip install -r requirements.txt`

### "Python is not recognized"
**Fix**:
- Reinstall Python
- Make sure to check "Add Python to PATH"

### Zox AI is slow
**Fix**:
- First command is always slower (loading model)
- Close other programs to free RAM
- Make sure you have 12GB+ RAM

---

## 📱 What Can Zox AI Do?

### Open Apps
- "Open Chrome"
- "Open Notepad"
- "Launch Calculator"

### Control Browser
- "Go to YouTube"
- "Search Google for cats"
- "Open Gmail"

### File Operations
- "Create a file called notes.txt"
- "Read the file notes.txt"

### System Control
- "What's my CPU usage?"
- "Take a screenshot"
- "Set volume to 50%"

### Mouse & Keyboard
- "Type 'Hello World'"
- "Move mouse to center"
- "Press enter"

**See `COMMANDS.md` for full list!**

---

## 🎯 Tips for Success

1. **Be Specific**: "Open Chrome" works better than "Open browser"
2. **Be Patient**: First command takes 5-10 seconds (loading AI)
3. **Use Text First**: Get comfortable with text before trying voice
4. **Check Status**: Look at the status label (bottom of window)
5. **Read Docs**: `COMMANDS.md` has tons of examples

---

## 🆘 Need Help?

### Quick Checks
1. Is Ollama running? (Check system tray)
2. Is Python installed? (`python --version`)
3. Are dependencies installed? (Run `install.bat`)

### Test Everything
```bash
python test_components.py
```

This will test all components and show what's working.

### Read Full Guide
See `SETUP_GUIDE.md` for detailed troubleshooting.

---

## 📚 Next Steps

### Learn More Commands
- Read `COMMANDS.md` for all available commands
- Try different combinations
- Experiment with system control

### Customize Zox AI
- Edit `config.py` to change settings
- Adjust voice speed and volume
- Change window size

### Advanced Features
- Schedule tasks
- Create custom workflows
- Add new commands (see documentation)

---

## 🎉 You're Ready!

That's it! You now have a fully functional AI assistant running on your computer.

**Try it now:**
1. Make sure Ollama is running
2. Run `python main.py` or `run.bat`
3. Type "Hello" in the chat
4. Watch Zox AI respond!

---

## 📊 System Requirements Reminder

- **OS**: Windows 10/11 (64-bit)
- **RAM**: 12GB minimum
- **Storage**: 10GB free space
- **Python**: 3.9 or higher

---

## 🔒 Privacy Note

✅ **100% Offline** - No internet needed after setup  
✅ **No Cloud** - Everything runs on your computer  
✅ **No API Keys** - No external services  
✅ **Your Data** - Stays on your computer  

---

## 🌟 Pro Tips

### Speed Up Responses
- Keep Ollama running in background
- Close unnecessary apps
- Use SSD if available

### Better Voice Recognition
- Speak clearly and at normal pace
- Use a good microphone
- Minimize background noise

### Organize Your Files
- Zox AI creates files in `Documents/Zox AI/`
- Screenshots go to `Pictures/Zox AI_Screenshots/`
- Logs are in `Documents/Zox AI/logs/`

---

## 🎓 Learning Path

1. **Day 1**: Basic commands (open apps, simple tasks)
2. **Day 2**: File operations and browser control
3. **Day 3**: System control and automation
4. **Day 4**: Voice input and advanced features
5. **Day 5**: Custom workflows and scheduling

---

## 📞 Quick Reference Card

```
┌─────────────────────────────────────┐
│         Zox AI QUICK REF            │
├─────────────────────────────────────┤
│ Start:     python main.py           │
│ Test:      python test_components.py│
│ Ollama:    ollama serve             │
│ Model:     llama3.1:8b-instruct...  │
│ Port:      localhost:11434          │
│ Files:     Documents/Zox AI/        │
│ Shots:     Pictures/Zox AI_Scree... │
│ Logs:      Documents/Zox AI/logs/   │
└─────────────────────────────────────┘
```

---

**Built by MrLexCoder** 🚀

*Your personal AI assistant, ready in 5 minutes!*

---

## ✅ Checklist

Before you start:
- [ ] Python installed
- [ ] Ollama installed
- [ ] Model downloaded
- [ ] Dependencies installed
- [ ] Ollama is running

Ready to go:
- [ ] Run `python main.py`
- [ ] GUI appears
- [ ] Type "Hello"
- [ ] Get response

**If all checked, you're good to go! 🎉**
