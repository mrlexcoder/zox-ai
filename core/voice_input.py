"""
Voice Input - Speech-to-Text using faster-whisper
Fully offline, runs on CPU
"""

import logging
import sounddevice as sd
import numpy as np
import wave
import tempfile
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from faster_whisper import WhisperModel
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    logger.warning("faster-whisper not available. Voice input will be disabled.")


class VoiceInput:
    """Speech-to-text using faster-whisper"""
    
    def __init__(self, model_size="base", device="cpu"):
        """
        Initialize voice input
        model_size: tiny, base, small, medium, large
        device: cpu or cuda
        """
        self.model = None
        self.sample_rate = 16000
        self.duration = 5  # seconds to record
        
        if WHISPER_AVAILABLE:
            try:
                logger.info(f"Loading Whisper model: {model_size}")
                self.model = WhisperModel(model_size, device=device, compute_type="int8")
                logger.info("Whisper model loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load Whisper model: {str(e)}")
                self.model = None
    
    def listen(self, duration=None):
        """
        Listen for voice input and convert to text
        Returns: transcribed text or None
        """
        if not self.model:
            logger.error("Whisper model not available")
            return None
        
        try:
            if duration is None:
                duration = self.duration
            
            logger.info(f"Recording for {duration} seconds...")
            
            # Record audio
            audio_data = sd.rec(
                int(duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype=np.int16
            )
            sd.wait()
            
            logger.info("Recording complete, transcribing...")
            
            # Save to temporary WAV file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            temp_path = temp_file.name
            temp_file.close()
            
            with wave.open(temp_path, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)  # 16-bit
                wf.setframerate(self.sample_rate)
                wf.writeframes(audio_data.tobytes())
            
            # Transcribe
            segments, info = self.model.transcribe(temp_path, beam_size=5)
            
            # Combine all segments
            text = " ".join([segment.text for segment in segments]).strip()
            
            # Clean up temp file
            try:
                os.unlink(temp_path)
            except:
                pass
            
            logger.info(f"Transcribed: {text}")
            return text if text else None
            
        except Exception as e:
            logger.error(f"Error during voice input: {str(e)}")
            return None
    
    def listen_continuous(self, callback, silence_threshold=500, silence_duration=2):
        """
        Continuous listening mode with voice activity detection
        callback: function to call with transcribed text
        """
        if not self.model:
            logger.error("Whisper model not available")
            return
        
        logger.info("Starting continuous listening mode...")
        
        try:
            # This is a simplified version - for production, use proper VAD
            while True:
                text = self.listen(duration=3)
                if text:
                    callback(text)
                    
        except KeyboardInterrupt:
            logger.info("Stopped continuous listening")


class VoiceInputSimulator:
    """Fallback simulator when faster-whisper is not available"""
    
    def listen(self, duration=None):
        """Simulate voice input with text input"""
        logger.warning("Using text input simulator (faster-whisper not available)")
        return input("Speak (type): ")
    
    def listen_continuous(self, callback, silence_threshold=500, silence_duration=2):
        """Simulate continuous listening"""
        while True:
            text = self.listen()
            if text:
                callback(text)


# Use simulator if faster-whisper is not available
if not WHISPER_AVAILABLE:
    VoiceInput = VoiceInputSimulator


if __name__ == "__main__":
    # Test voice input
    print("Testing voice input...")
    
    voice = VoiceInput(model_size="base")
    
    print("Speak now...")
    text = voice.listen(duration=5)
    
    if text:
        print(f"You said: {text}")
    else:
        print("No speech detected")
