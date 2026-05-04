"""
Voice Output - Text-to-Speech using pyttsx3
Fully offline
"""

import pyttsx3
import logging
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VoiceOutput:
    """Text-to-speech using pyttsx3"""
    
    def __init__(self, rate=150, volume=0.9, voice_index=0):
        """
        Initialize voice output
        rate: speech rate (words per minute)
        volume: 0.0 to 1.0
        voice_index: 0 for male, 1 for female (if available)
        """
        try:
            self.engine = pyttsx3.init()
            
            # Set properties
            self.engine.setProperty('rate', rate)
            self.engine.setProperty('volume', volume)
            
            # Get available voices
            voices = self.engine.getProperty('voices')
            if voices and len(voices) > voice_index:
                self.engine.setProperty('voice', voices[voice_index].id)
                logger.info(f"Using voice: {voices[voice_index].name}")
            
            self.is_speaking = False
            logger.info("Voice output initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize voice output: {str(e)}")
            self.engine = None
    
    def speak(self, text, blocking=False):
        """
        Speak the given text
        text: text to speak
        blocking: if True, wait for speech to complete
        """
        if not self.engine:
            logger.error("Voice engine not available")
            return
        
        if not text:
            return
        
        try:
            logger.info(f"Speaking: {text}")
            
            if blocking:
                self.engine.say(text)
                self.engine.runAndWait()
            else:
                # Speak in separate thread to avoid blocking
                thread = threading.Thread(target=self._speak_thread, args=(text,))
                thread.daemon = True
                thread.start()
                
        except Exception as e:
            logger.error(f"Error during speech: {str(e)}")
    
    def _speak_thread(self, text):
        """Internal method to speak in a separate thread"""
        try:
            self.is_speaking = True
            self.engine.say(text)
            self.engine.runAndWait()
            self.is_speaking = False
        except Exception as e:
            logger.error(f"Error in speech thread: {str(e)}")
            self.is_speaking = False
    
    def stop(self):
        """Stop current speech"""
        if self.engine:
            try:
                self.engine.stop()
                self.is_speaking = False
            except Exception as e:
                logger.error(f"Error stopping speech: {str(e)}")
    
    def set_rate(self, rate):
        """Set speech rate (words per minute)"""
        if self.engine:
            self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume):
        """Set volume (0.0 to 1.0)"""
        if self.engine:
            self.engine.setProperty('volume', max(0.0, min(1.0, volume)))
    
    def set_voice(self, voice_index):
        """Change voice"""
        if self.engine:
            voices = self.engine.getProperty('voices')
            if voices and len(voices) > voice_index:
                self.engine.setProperty('voice', voices[voice_index].id)
    
    def list_voices(self):
        """List available voices"""
        if self.engine:
            voices = self.engine.getProperty('voices')
            return [(i, v.name, v.id) for i, v in enumerate(voices)]
        return []


if __name__ == "__main__":
    # Test voice output
    print("Testing voice output...")
    
    voice = VoiceOutput()
    
    # List available voices
    print("\nAvailable voices:")
    for idx, name, voice_id in voice.list_voices():
        print(f"{idx}: {name}")
    
    # Test speech
    print("\nSpeaking test message...")
    voice.speak("Hello! I am Zox AI, your AI assistant. How can I help you today?", blocking=True)
    
    print("Done!")
