"""
Mouse and Keyboard Control - Human-like input simulation
Uses pyautogui for realistic delays and movements
"""

import pyautogui
import time
import logging
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Safety settings
pyautogui.FAILSAFE = True  # Move mouse to corner to abort
pyautogui.PAUSE = 0.1  # Pause between actions


class MouseKeyboardController:
    """Control mouse and keyboard with human-like behavior"""
    
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        logger.info(f"Screen size: {self.screen_width}x{self.screen_height}")
    
    # ===== KEYBOARD CONTROL =====
    
    def type_text(self, text, interval=0.05, human_like=True):
        """
        Type text with realistic delays
        text: text to type
        interval: base delay between keystrokes
        human_like: add random variation to delays
        """
        try:
            logger.info(f"Typing: {text}")
            
            if human_like:
                # Type with random delays for human-like effect
                for char in text:
                    pyautogui.write(char, interval=0)
                    delay = interval + random.uniform(-0.02, 0.03)
                    time.sleep(max(0.01, delay))
            else:
                pyautogui.write(text, interval=interval)
            
            logger.info("Typing complete")
            return True
            
        except Exception as e:
            logger.error(f"Error typing text: {str(e)}")
            return False
    
    def press_key(self, key, presses=1, interval=0.1):
        """
        Press a key one or more times
        key: key name (e.g., 'enter', 'space', 'tab', 'esc', 'a', 'ctrl')
        presses: number of times to press
        interval: delay between presses
        """
        try:
            logger.info(f"Pressing key: {key} ({presses} times)")
            pyautogui.press(key, presses=presses, interval=interval)
            return True
        except Exception as e:
            logger.error(f"Error pressing key {key}: {str(e)}")
            return False
    
    def hotkey(self, *keys):
        """
        Press a combination of keys (e.g., Ctrl+C)
        keys: key names to press together
        """
        try:
            logger.info(f"Pressing hotkey: {'+'.join(keys)}")
            pyautogui.hotkey(*keys)
            return True
        except Exception as e:
            logger.error(f"Error pressing hotkey: {str(e)}")
            return False
    
    def hold_key(self, key, duration=1.0):
        """
        Hold a key for a duration
        key: key to hold
        duration: how long to hold (seconds)
        """
        try:
            logger.info(f"Holding key: {key} for {duration}s")
            pyautogui.keyDown(key)
            time.sleep(duration)
            pyautogui.keyUp(key)
            return True
        except Exception as e:
            logger.error(f"Error holding key {key}: {str(e)}")
            return False
    
    # ===== MOUSE CONTROL =====
    
    def move_mouse(self, x, y, duration=0.5, human_like=True):
        """
        Move mouse to position
        x, y: target coordinates
        duration: time to move (seconds)
        human_like: use curved path instead of straight line
        """
        try:
            logger.info(f"Moving mouse to ({x}, {y})")
            
            if human_like:
                # Add slight curve to movement
                pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)
            else:
                pyautogui.moveTo(x, y, duration=duration)
            
            return True
        except Exception as e:
            logger.error(f"Error moving mouse: {str(e)}")
            return False
    
    def move_mouse_relative(self, dx, dy, duration=0.5):
        """
        Move mouse relative to current position
        dx, dy: relative movement
        duration: time to move (seconds)
        """
        try:
            logger.info(f"Moving mouse by ({dx}, {dy})")
            pyautogui.moveRel(dx, dy, duration=duration)
            return True
        except Exception as e:
            logger.error(f"Error moving mouse relatively: {str(e)}")
            return False
    
    def click_mouse(self, button='left', clicks=1, interval=0.1, x=None, y=None):
        """
        Click mouse button
        button: 'left', 'right', or 'middle'
        clicks: number of clicks (2 for double-click)
        interval: delay between clicks
        x, y: optional position to click at
        """
        try:
            if x is not None and y is not None:
                logger.info(f"Clicking {button} button at ({x}, {y})")
                pyautogui.click(x=x, y=y, clicks=clicks, interval=interval, button=button)
            else:
                logger.info(f"Clicking {button} button")
                pyautogui.click(clicks=clicks, interval=interval, button=button)
            
            return True
        except Exception as e:
            logger.error(f"Error clicking mouse: {str(e)}")
            return False
    
    def drag_mouse(self, x, y, duration=0.5, button='left'):
        """
        Drag mouse to position
        x, y: target coordinates
        duration: time to drag (seconds)
        button: mouse button to hold
        """
        try:
            logger.info(f"Dragging mouse to ({x}, {y})")
            pyautogui.drag(x, y, duration=duration, button=button)
            return True
        except Exception as e:
            logger.error(f"Error dragging mouse: {str(e)}")
            return False
    
    def scroll(self, clicks, direction='vertical'):
        """
        Scroll mouse wheel
        clicks: amount to scroll (positive = up/right, negative = down/left)
        direction: 'vertical' or 'horizontal'
        """
        try:
            logger.info(f"Scrolling {direction}: {clicks}")
            
            if direction == 'vertical':
                pyautogui.scroll(clicks)
            else:
                pyautogui.hscroll(clicks)
            
            return True
        except Exception as e:
            logger.error(f"Error scrolling: {str(e)}")
            return False
    
    def get_mouse_position(self):
        """
        Get current mouse position
        Returns: (x, y) tuple
        """
        try:
            pos = pyautogui.position()
            return (pos.x, pos.y)
        except Exception as e:
            logger.error(f"Error getting mouse position: {str(e)}")
            return None
    
    # ===== SCREEN UTILITIES =====
    
    def get_screen_size(self):
        """
        Get screen dimensions
        Returns: (width, height) tuple
        """
        return (self.screen_width, self.screen_height)
    
    def move_to_center(self):
        """Move mouse to center of screen"""
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        return self.move_mouse(center_x, center_y)
    
    # ===== COMMON ACTIONS =====
    
    def copy(self):
        """Perform Ctrl+C"""
        return self.hotkey('ctrl', 'c')
    
    def paste(self):
        """Perform Ctrl+V"""
        return self.hotkey('ctrl', 'v')
    
    def cut(self):
        """Perform Ctrl+X"""
        return self.hotkey('ctrl', 'x')
    
    def select_all(self):
        """Perform Ctrl+A"""
        return self.hotkey('ctrl', 'a')
    
    def undo(self):
        """Perform Ctrl+Z"""
        return self.hotkey('ctrl', 'z')
    
    def redo(self):
        """Perform Ctrl+Y"""
        return self.hotkey('ctrl', 'y')
    
    def save(self):
        """Perform Ctrl+S"""
        return self.hotkey('ctrl', 's')
    
    def find(self):
        """Perform Ctrl+F"""
        return self.hotkey('ctrl', 'f')
    
    def new_tab(self):
        """Perform Ctrl+T (new tab in browser)"""
        return self.hotkey('ctrl', 't')
    
    def close_tab(self):
        """Perform Ctrl+W (close tab)"""
        return self.hotkey('ctrl', 'w')
    
    def alt_tab(self):
        """Switch windows with Alt+Tab"""
        return self.hotkey('alt', 'tab')
    
    def show_desktop(self):
        """Show desktop (Win+D)"""
        return self.hotkey('win', 'd')
    
    def take_screenshot_region(self, x, y, width, height):
        """
        Take screenshot of a region
        Returns: PIL Image object
        """
        try:
            logger.info(f"Taking screenshot of region ({x}, {y}, {width}, {height})")
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            return screenshot
        except Exception as e:
            logger.error(f"Error taking screenshot: {str(e)}")
            return None
    
    def locate_on_screen(self, image_path, confidence=0.8):
        """
        Find an image on screen
        image_path: path to image to find
        confidence: matching confidence (0.0 to 1.0)
        Returns: (x, y, width, height) or None
        """
        try:
            logger.info(f"Locating image on screen: {image_path}")
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            return location
        except Exception as e:
            logger.error(f"Error locating image: {str(e)}")
            return None
    
    def click_image(self, image_path, confidence=0.8):
        """
        Find and click an image on screen
        image_path: path to image to find and click
        confidence: matching confidence (0.0 to 1.0)
        """
        try:
            location = self.locate_on_screen(image_path, confidence)
            if location:
                center = pyautogui.center(location)
                return self.click_mouse(x=center.x, y=center.y)
            else:
                logger.warning(f"Image not found: {image_path}")
                return False
        except Exception as e:
            logger.error(f"Error clicking image: {str(e)}")
            return False


if __name__ == "__main__":
    # Test mouse and keyboard controller
    controller = MouseKeyboardController()
    
    print(f"Screen size: {controller.get_screen_size()}")
    print(f"Mouse position: {controller.get_mouse_position()}")
    
    print("\nTesting keyboard...")
    controller.type_text("Hello from Zox AI!", interval=0.1, human_like=True)
    
    print("\nTesting mouse...")
    controller.move_to_center()
    
    print("\nDone!")
