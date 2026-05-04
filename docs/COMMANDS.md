# Zox AI Command Reference
**Quick reference for all available commands**

## 🎤 Voice Commands

Just click "Start Listening" and speak naturally!

---

## 📱 Application Control

### Open Applications
- "Open Chrome"
- "Open Notepad"
- "Open Calculator"
- "Open File Explorer"
- "Launch Visual Studio Code"
- "Start Spotify"

### Close Applications
- "Close Chrome"
- "Close Notepad"
- "Quit Calculator"

### Supported Apps
- Chrome, Firefox, Edge (browsers)
- Notepad, WordPad (text editors)
- Calculator
- File Explorer
- Paint
- Task Manager
- Control Panel
- Settings
- VS Code, Spotify, Discord, Slack, Teams (if installed)

---

## 📁 File Operations

### Create Files
- "Create a file called notes.txt"
- "Create a file named todo.txt with my tasks"
- "Make a new file test.py with print hello"

### Read Files
- "Read the file notes.txt"
- "Show me what's in todo.txt"
- "Open and read test.py"

### Delete Files
- "Delete the file notes.txt"
- "Remove test.py"

**Note**: Files are created in `Documents/Zox AI/` by default

---

## 🖱️ Mouse Control

### Move Mouse
- "Move mouse to center"
- "Move mouse to position 500, 300"
- "Move cursor to top left"

### Click
- "Click left mouse button"
- "Right click"
- "Double click"
- "Click at position 100, 200"

### Scroll
- "Scroll down"
- "Scroll up"
- "Scroll down 5 times"

---

## ⌨️ Keyboard Control

### Type Text
- "Type 'Hello World'"
- "Type 'This is a test' slowly"
- "Write 'Python is awesome'"

### Press Keys
- "Press enter"
- "Press tab"
- "Press escape"
- "Press space"

### Keyboard Shortcuts
- "Press Ctrl+C" (copy)
- "Press Ctrl+V" (paste)
- "Press Ctrl+S" (save)
- "Press Alt+Tab" (switch windows)
- "Press Win+D" (show desktop)

---

## 🌐 Browser Control

### Open Websites
- "Open YouTube"
- "Go to GitHub"
- "Open Gmail"
- "Visit Reddit"
- "Open Wikipedia"

### Open URLs
- "Open https://google.com"
- "Go to example.com"

### Search
- "Search Google for Python tutorials"
- "Search YouTube for music"

### Browser Actions
- "Refresh page"
- "Go back"
- "Go forward"
- "New tab"
- "Close tab"
- "Zoom in"
- "Zoom out"

### Supported Sites
YouTube, Gmail, GitHub, Reddit, Twitter, Facebook, Instagram, LinkedIn, Stack Overflow, Wikipedia, Amazon, Netflix, Spotify, Twitch, Discord

---

## 🖥️ System Control

### System Information
- "What's my CPU usage?"
- "How much RAM am I using?"
- "Check disk space"
- "Show system info"
- "What's my battery level?" (laptops)

### Volume Control
- "Set volume to 50%"
- "Increase volume"
- "Decrease volume"
- "Mute"
- "Unmute"

### Brightness Control
- "Set brightness to 75%"
- "Increase brightness"
- "Decrease brightness"

### Screenshots
- "Take a screenshot"
- "Capture screen"
- "Screenshot"

**Note**: Screenshots saved to `Pictures/Zox AI_Screenshots/`

---

## ⏰ Task Scheduling

### Schedule Tasks
- "Schedule a task at 14:30 to remind me"
- "Set a reminder for 3 PM"
- "Schedule opening Chrome at 9 AM"

### Recurring Tasks
- "Run this every 5 minutes"
- "Repeat every hour"

---

## 💬 Conversation

### Greetings
- "Hello"
- "Hi Zox AI"
- "Good morning"

### Questions
- "What can you do?"
- "Help me"
- "What time is it?"

### Status
- "Are you there?"
- "How are you?"

---

## 🎯 Example Workflows

### Workflow 1: Research Session
1. "Open Chrome"
2. "Go to YouTube"
3. "Search Google for Python tutorials"
4. "Take a screenshot"

### Workflow 2: Note Taking
1. "Open Notepad"
2. "Type 'Meeting Notes'"
3. "Press enter twice"
4. "Type 'Attendees: John, Sarah'"

### Workflow 3: System Check
1. "What's my CPU usage?"
2. "Check RAM"
3. "Take a screenshot"
4. "Create a file called system_report.txt"

### Workflow 4: Productivity
1. "Set volume to 30%"
2. "Open VS Code"
3. "Open Chrome and go to GitHub"
4. "Set brightness to 80%"

---

## 🔧 Advanced Commands

### Combine Multiple Actions
- "Open Chrome and go to YouTube"
- "Create a file called test.txt with hello world"
- "Move mouse to center and click"

### Precise Control
- "Type 'Hello' with 0.1 second delay between keys"
- "Move mouse to 1920, 1080 in 2 seconds"
- "Click at position 500, 500"

---

## 💡 Tips

1. **Be Natural**: Speak naturally, Zox AI understands context
2. **Be Specific**: "Open Chrome" is better than "Open browser"
3. **Combine Actions**: You can chain multiple commands
4. **Use Shortcuts**: Zox AI knows common keyboard shortcuts
5. **Check Status**: Ask about system info anytime

---

## 🚫 Limitations

- Cannot access password-protected files
- Cannot perform actions requiring admin rights (unless run as admin)
- Voice recognition works best in quiet environments
- Some apps may need full path if not in system PATH

---

## 🆘 Troubleshooting Commands

If Zox AI doesn't understand:
1. Try rephrasing the command
2. Be more specific
3. Use simpler language
4. Check if the app/file exists

Example:
- ❌ "Do the thing" (too vague)
- ✅ "Open Chrome" (specific)

---

## 📝 Command Format

### General Pattern
```
[Action] [Target] [Optional: Details]
```

Examples:
- **Open** Chrome
- **Create** a file **called** notes.txt **with** hello world
- **Set** volume **to** 50%
- **Move** mouse **to** center

---

## 🎨 Customization

Want to add custom commands? Edit:
- `core/llm.py` - Add new intents
- `main.py` - Add execution logic
- `actions/` - Add new action handlers

---

**Built by MrLexCoder** 🚀

For more help, see `SETUP_GUIDE.md` or `README.md`
