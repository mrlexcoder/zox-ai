"""
Zox AI - Offline AI Desktop Assistant
Built by MrLexCoder
Main entry point with PyQt6 GUI
"""

import sys
import json
import threading
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTextEdit, QLineEdit, QPushButton, 
                             QLabel, QFrame)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt6.QtGui import QFont, QTextCursor

from core.llm import LLMEngine
from core.voice_input import VoiceInput
from core.voice_output import VoiceOutput
from actions.app_control import AppController
from actions.file_control import FileController
from actions.mouse_keyboard import MouseKeyboardController
from actions.browser_control import BrowserController
from actions.system_control import SystemController
from actions.scheduler import TaskScheduler


class SignalEmitter(QObject):
    """Signal emitter for thread-safe GUI updates"""
    message_signal = pyqtSignal(str, str)  # (role, message)
    status_signal = pyqtSignal(str)


class Zox AIGUI(QMainWindow):
    """Main Zox AI GUI - Floating chat window"""
    
    def __init__(self):
        super().__init__()
        self.signal_emitter = SignalEmitter()
        self.signal_emitter.message_signal.connect(self.add_message_to_chat)
        self.signal_emitter.status_signal.connect(self.update_status)
        
        # Initialize components
        self.llm = LLMEngine()
        self.voice_input = VoiceInput()
        self.voice_output = VoiceOutput()
        
        # Initialize action controllers
        self.app_controller = AppController()
        self.file_controller = FileController()
        self.mouse_keyboard = MouseKeyboardController()
        self.browser_controller = BrowserController()
        self.system_controller = SystemController()
        self.scheduler = TaskScheduler()
        
        self.is_listening = False
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Zox AI - AI Assistant by MrLexCoder")
        self.setGeometry(100, 100, 500, 700)
        
        # Make window stay on top and frameless for modern look
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Container frame for rounded corners
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border-radius: 15px;
                border: 2px solid #00ff41;
            }
        """)
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)
        
        # Header
        header_layout = QHBoxLayout()
        title_label = QLabel("🤖 Zox AI")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #00ff41; border: none;")
        
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff4444;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #ff6666;
            }
        """)
        close_btn.clicked.connect(self.close)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(close_btn)
        container_layout.addLayout(header_layout)
        
        # Status label
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("color: #00ff41; font-size: 12px; border: none;")
        container_layout.addWidget(self.status_label)
        
        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #00ff41;
                border-radius: 10px;
                padding: 10px;
                font-size: 13px;
            }
        """)
        container_layout.addWidget(self.chat_display)
        
        # Input area
        input_layout = QHBoxLayout()
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your command...")
        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #00ff41;
                border-radius: 10px;
                padding: 10px;
                font-size: 13px;
            }
        """)
        self.input_field.returnPressed.connect(self.send_message)
        
        send_btn = QPushButton("Send")
        send_btn.setStyleSheet("""
            QPushButton {
                background-color: #00ff41;
                color: #000000;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00cc33;
            }
        """)
        send_btn.clicked.connect(self.send_message)
        
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(send_btn)
        container_layout.addLayout(input_layout)
        
        # Voice control buttons
        voice_layout = QHBoxLayout()
        
        self.voice_btn = QPushButton("🎤 Start Listening")
        self.voice_btn.setStyleSheet("""
            QPushButton {
                background-color: #0066ff;
                color: #ffffff;
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0052cc;
            }
        """)
        self.voice_btn.clicked.connect(self.toggle_voice_input)
        
        voice_layout.addWidget(self.voice_btn)
        container_layout.addLayout(voice_layout)
        
        main_layout.addWidget(container)
        central_widget.setLayout(main_layout)
        
        # Add welcome message
        self.add_message_to_chat("Zox AI", "Hello! I'm Zox AI, your offline AI assistant. How can I help you today?")
        
    def mousePressEvent(self, event):
        """Enable window dragging"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
            
    def mouseMoveEvent(self, event):
        """Handle window dragging"""
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()
    
    def add_message_to_chat(self, role, message):
        """Add a message to the chat display"""
        color = "#00ff41" if role == "Zox AI" else "#ffffff"
        self.chat_display.append(f'<span style="color: {color}; font-weight: bold;">{role}:</span> {message}<br>')
        self.chat_display.moveCursor(QTextCursor.MoveOperation.End)
    
    def update_status(self, status):
        """Update status label"""
        self.status_label.setText(status)
    
    def send_message(self):
        """Send user message and get response"""
        user_input = self.input_field.text().strip()
        if not user_input:
            return
        
        self.input_field.clear()
        self.add_message_to_chat("You", user_input)
        
        # Process in separate thread to avoid blocking GUI
        threading.Thread(target=self.process_command, args=(user_input,), daemon=True).start()
    
    def process_command(self, user_input):
        """Process user command with LLM and execute actions"""
        try:
            self.signal_emitter.status_signal.emit("Thinking...")
            
            # Get action plan from LLM
            action_plan = self.llm.get_action_plan(user_input)
            
            if not action_plan:
                self.signal_emitter.message_signal.emit("Zox AI", "I couldn't understand that. Could you rephrase?")
                self.signal_emitter.status_signal.emit("Ready")
                return
            
            # Execute actions
            response = self.execute_actions(action_plan)
            
            # Speak response
            self.voice_output.speak(response)
            
            self.signal_emitter.message_signal.emit("Zox AI", response)
            self.signal_emitter.status_signal.emit("Ready")
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.signal_emitter.message_signal.emit("Zox AI", error_msg)
            self.signal_emitter.status_signal.emit("Error")
    
    def execute_actions(self, action_plan):
        """Execute the action plan from LLM"""
        try:
            actions = action_plan.get("actions", [])
            response_text = action_plan.get("response", "Done!")
            
            for action in actions:
                intent = action.get("intent", "")
                
                # App control
                if intent == "open_app":
                    self.app_controller.open_app(action.get("app"))
                elif intent == "close_app":
                    self.app_controller.close_app(action.get("app"))
                
                # File control
                elif intent == "create_file":
                    self.file_controller.create_file(action.get("path"), action.get("content", ""))
                elif intent == "delete_file":
                    self.file_controller.delete_file(action.get("path"))
                elif intent == "read_file":
                    content = self.file_controller.read_file(action.get("path"))
                    response_text = f"File content:\n{content}"
                
                # Mouse and keyboard
                elif intent == "type_text":
                    self.mouse_keyboard.type_text(action.get("text"), action.get("interval", 0.05))
                elif intent == "move_mouse":
                    self.mouse_keyboard.move_mouse(action.get("x"), action.get("y"))
                elif intent == "click_mouse":
                    self.mouse_keyboard.click_mouse(action.get("button", "left"))
                elif intent == "press_key":
                    self.mouse_keyboard.press_key(action.get("key"))
                
                # Browser control
                elif intent == "open_url":
                    self.browser_controller.open_url(action.get("url"))
                
                # System control
                elif intent == "screenshot":
                    path = self.system_controller.take_screenshot(action.get("path", "screenshot.png"))
                    response_text = f"Screenshot saved to {path}"
                elif intent == "set_volume":
                    self.system_controller.set_volume(action.get("level"))
                elif intent == "set_brightness":
                    self.system_controller.set_brightness(action.get("level"))
                elif intent == "get_system_info":
                    info = self.system_controller.get_system_info()
                    response_text = f"CPU: {info['cpu']}%, RAM: {info['ram']}%, Disk: {info['disk']}%"
                
                # Scheduler
                elif intent == "schedule_task":
                    self.scheduler.schedule_task(action.get("time"), action.get("command"))
                    response_text = f"Task scheduled for {action.get('time')}"
            
            return response_text
            
        except Exception as e:
            return f"Error executing actions: {str(e)}"
    
    def toggle_voice_input(self):
        """Toggle voice input on/off"""
        if not self.is_listening:
            self.is_listening = True
            self.voice_btn.setText("🎤 Listening...")
            self.voice_btn.setStyleSheet("""
                QPushButton {
                    background-color: #ff0000;
                    color: #ffffff;
                    border: none;
                    border-radius: 10px;
                    padding: 10px;
                    font-weight: bold;
                }
            """)
            threading.Thread(target=self.listen_voice, daemon=True).start()
        else:
            self.is_listening = False
            self.voice_btn.setText("🎤 Start Listening")
            self.voice_btn.setStyleSheet("""
                QPushButton {
                    background-color: #0066ff;
                    color: #ffffff;
                    border: none;
                    border-radius: 10px;
                    padding: 10px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #0052cc;
                }
            """)
    
    def listen_voice(self):
        """Listen for voice input"""
        try:
            self.signal_emitter.status_signal.emit("Listening...")
            text = self.voice_input.listen()
            
            if text:
                self.signal_emitter.message_signal.emit("You", text)
                self.process_command(text)
            
            self.is_listening = False
            self.signal_emitter.status_signal.emit("Ready")
            
            # Reset button
            self.voice_btn.setText("🎤 Start Listening")
            self.voice_btn.setStyleSheet("""
                QPushButton {
                    background-color: #0066ff;
                    color: #ffffff;
                    border: none;
                    border-radius: 10px;
                    padding: 10px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #0052cc;
                }
            """)
            
        except Exception as e:
            self.signal_emitter.message_signal.emit("Zox AI", f"Voice input error: {str(e)}")
            self.is_listening = False


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle("Fusion")
    
    # Create and show GUI
    zoxai = Zox AIGUI()
    zoxai.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
