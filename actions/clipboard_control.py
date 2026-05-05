"""
Clipboard Control - Copy, paste, and manage clipboard
"""

import logging
import pyperclip

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClipboardController:
    """Control clipboard operations"""
    
    def __init__(self):
        logger.info("Clipboard controller initialized")
    
    def copy_text(self, text):
        """
        Copy text to clipboard
        text: text to copy
        """
        try:
            pyperclip.copy(text)
            logger.info(f"Copied to clipboard: {text[:50]}...")
            return True
        except Exception as e:
            logger.error(f"Error copying to clipboard: {str(e)}")
            return False
    
    def paste_text(self):
        """
        Get text from clipboard
        Returns: clipboard text or None
        """
        try:
            text = pyperclip.paste()
            logger.info(f"Pasted from clipboard: {text[:50]}...")
            return text
        except Exception as e:
            logger.error(f"Error pasting from clipboard: {str(e)}")
            return None
    
    def clear_clipboard(self):
        """Clear clipboard"""
        try:
            pyperclip.copy('')
            logger.info("Clipboard cleared")
            return True
        except Exception as e:
            logger.error(f"Error clearing clipboard: {str(e)}")
            return False
    
    def get_clipboard_history(self):
        """
        Get current clipboard content
        Returns: dict with clipboard info
        """
        try:
            text = pyperclip.paste()
            return {
                'text': text,
                'length': len(text),
                'has_content': bool(text)
            }
        except Exception as e:
            logger.error(f"Error getting clipboard info: {str(e)}")
            return {}


if __name__ == "__main__":
    # Test clipboard controller
    clipboard = ClipboardController()
    
    print("Testing clipboard...")
    
    # Copy text
    clipboard.copy_text("Hello from Zox AI!")
    
    # Paste text
    text = clipboard.paste_text()
    print(f"Clipboard content: {text}")
    
    # Get info
    info = clipboard.get_clipboard_history()
    print(f"Clipboard info: {info}")
    
    print("Done!")
