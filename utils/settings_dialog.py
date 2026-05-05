"""
Settings Dialog - GUI for configuring Zox AI
"""

from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QSpinBox, QDoubleSpinBox, QCheckBox,
                             QPushButton, QTabWidget, QWidget, QComboBox,
                             QGroupBox, QFormLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import config


class SettingsDialog(QDialog):
    """Settings dialog for Zox AI"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Zox AI Settings")
        self.setMinimumSize(600, 500)
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("⚙️ Zox AI Settings")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setStyleSheet("color: #00ff41; margin: 10px;")
        layout.addWidget(title)
        
        # Tabs
        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #00ff41;
                background: #2d2d2d;
            }
            QTabBar::tab {
                background: #1e1e1e;
                color: #ffffff;
                padding: 10px 20px;
                margin: 2px;
            }
            QTabBar::tab:selected {
                background: #00ff41;
                color: #000000;
            }
        """)
        
        # Voice Settings Tab
        voice_tab = self.create_voice_settings()
        tabs.addTab(voice_tab, "🎤 Voice")
        
        # LLM Settings Tab
        llm_tab = self.create_llm_settings()
        tabs.addTab(llm_tab, "🧠 AI Model")
        
        # GUI Settings Tab
        gui_tab = self.create_gui_settings()
        tabs.addTab(gui_tab, "💬 Interface")
        
        # System Settings Tab
        system_tab = self.create_system_settings()
        tabs.addTab(system_tab, "🖥️ System")
        
        layout.addWidget(tabs)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_btn = QPushButton("💾 Save")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #00ff41;
                color: #000000;
                border: none;
                border-radius: 5px;
                padding: 10px 30px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00cc33;
            }
        """)
        save_btn.clicked.connect(self.save_settings)
        
        cancel_btn = QPushButton("❌ Cancel")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff4444;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 10px 30px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff6666;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addStretch()
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        self.setStyleSheet("QDialog { background-color: #1e1e1e; }")
    
    def create_voice_settings(self):
        """Create voice settings tab"""
        widget = QWidget()
        layout = QFormLayout()
        
        # Voice rate
        self.voice_rate = QSpinBox()
        self.voice_rate.setRange(50, 300)
        self.voice_rate.setValue(config.VOICE_RATE)
        layout.addRow("Voice Speed (WPM):", self.voice_rate)
        
        # Voice volume
        self.voice_volume = QDoubleSpinBox()
        self.voice_volume.setRange(0.0, 1.0)
        self.voice_volume.setSingleStep(0.1)
        self.voice_volume.setValue(config.VOICE_VOLUME)
        layout.addRow("Voice Volume:", self.voice_volume)
        
        # Whisper model
        self.whisper_model = QComboBox()
        self.whisper_model.addItems(["tiny", "base", "small", "medium", "large"])
        self.whisper_model.setCurrentText(config.WHISPER_MODEL_SIZE)
        layout.addRow("Whisper Model:", self.whisper_model)
        
        # Recording duration
        self.recording_duration = QSpinBox()
        self.recording_duration.setRange(1, 30)
        self.recording_duration.setValue(config.RECORDING_DURATION)
        layout.addRow("Recording Duration (s):", self.recording_duration)
        
        widget.setLayout(layout)
        return widget
    
    def create_llm_settings(self):
        """Create LLM settings tab"""
        widget = QWidget()
        layout = QFormLayout()
        
        # Ollama URL
        self.ollama_url = QLineEdit(config.OLLAMA_BASE_URL)
        layout.addRow("Ollama URL:", self.ollama_url)
        
        # Model name
        self.ollama_model = QLineEdit(config.OLLAMA_MODEL)
        layout.addRow("Model Name:", self.ollama_model)
        
        # Temperature
        self.llm_temperature = QDoubleSpinBox()
        self.llm_temperature.setRange(0.0, 2.0)
        self.llm_temperature.setSingleStep(0.1)
        self.llm_temperature.setValue(config.LLM_TEMPERATURE)
        layout.addRow("Temperature:", self.llm_temperature)
        
        # Max tokens
        self.llm_max_tokens = QSpinBox()
        self.llm_max_tokens.setRange(100, 2000)
        self.llm_max_tokens.setValue(config.LLM_MAX_TOKENS)
        layout.addRow("Max Tokens:", self.llm_max_tokens)
        
        widget.setLayout(layout)
        return widget
    
    def create_gui_settings(self):
        """Create GUI settings tab"""
        widget = QWidget()
        layout = QFormLayout()
        
        # Window size
        self.window_width = QSpinBox()
        self.window_width.setRange(300, 1920)
        self.window_width.setValue(config.WINDOW_WIDTH)
        layout.addRow("Window Width:", self.window_width)
        
        self.window_height = QSpinBox()
        self.window_height.setRange(400, 1080)
        self.window_height.setValue(config.WINDOW_HEIGHT)
        layout.addRow("Window Height:", self.window_height)
        
        widget.setLayout(layout)
        return widget
    
    def create_system_settings(self):
        """Create system settings tab"""
        widget = QWidget()
        layout = QFormLayout()
        
        # Enable features
        self.enable_voice_input = QCheckBox()
        self.enable_voice_input.setChecked(config.ENABLE_VOICE_INPUT)
        layout.addRow("Enable Voice Input:", self.enable_voice_input)
        
        self.enable_voice_output = QCheckBox()
        self.enable_voice_output.setChecked(config.ENABLE_VOICE_OUTPUT)
        layout.addRow("Enable Voice Output:", self.enable_voice_output)
        
        self.enable_scheduler = QCheckBox()
        self.enable_scheduler.setChecked(config.ENABLE_SCHEDULER)
        layout.addRow("Enable Scheduler:", self.enable_scheduler)
        
        # Max RAM
        self.max_ram = QSpinBox()
        self.max_ram.setRange(4, 32)
        self.max_ram.setValue(config.MAX_RAM_GB)
        layout.addRow("Max RAM (GB):", self.max_ram)
        
        widget.setLayout(layout)
        return widget
    
    def save_settings(self):
        """Save settings"""
        # Update config values
        config.VOICE_RATE = self.voice_rate.value()
        config.VOICE_VOLUME = self.voice_volume.value()
        config.WHISPER_MODEL_SIZE = self.whisper_model.currentText()
        config.RECORDING_DURATION = self.recording_duration.value()
        
        config.OLLAMA_BASE_URL = self.ollama_url.text()
        config.OLLAMA_MODEL = self.ollama_model.text()
        config.LLM_TEMPERATURE = self.llm_temperature.value()
        config.LLM_MAX_TOKENS = self.llm_max_tokens.value()
        
        config.WINDOW_WIDTH = self.window_width.value()
        config.WINDOW_HEIGHT = self.window_height.value()
        
        config.ENABLE_VOICE_INPUT = self.enable_voice_input.isChecked()
        config.ENABLE_VOICE_OUTPUT = self.enable_voice_output.isChecked()
        config.ENABLE_SCHEDULER = self.enable_scheduler.isChecked()
        config.MAX_RAM_GB = self.max_ram.value()
        
        self.accept()
