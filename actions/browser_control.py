"""
Browser Control - Open URLs and control browser
Uses webbrowser module and pyautogui for automation
"""

import webbrowser
import logging
import time
import pyautogui

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BrowserController:
    """Control web browser"""
    
    def __init__(self, default_browser=None):
        """
        Initialize browser controller
        default_browser: browser name (chrome, firefox, edge) or None for system default
        """
        self.default_browser = default_browser
        
        # Browser executable names
        self.browsers = {
            'chrome': 'chrome',
            'firefox': 'firefox',
            'edge': 'microsoft-edge',
            'safari': 'safari',
            'opera': 'opera'
        }
        
        # Register browsers
        if default_browser and default_browser.lower() in self.browsers:
            try:
                browser_name = self.browsers[default_browser.lower()]
                webbrowser.get(browser_name)
                logger.info(f"Using browser: {default_browser}")
            except:
                logger.warning(f"Could not find {default_browser}, using system default")
    
    def open_url(self, url, new_window=False, new_tab=True):
        """
        Open a URL in browser
        url: URL to open
        new_window: open in new window
        new_tab: open in new tab (if new_window is False)
        """
        try:
            # Ensure URL has protocol
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            logger.info(f"Opening URL: {url}")
            
            if new_window:
                webbrowser.open_new(url)
            elif new_tab:
                webbrowser.open_new_tab(url)
            else:
                webbrowser.open(url)
            
            return True
            
        except Exception as e:
            logger.error(f"Error opening URL {url}: {str(e)}")
            return False
    
    def search_google(self, query):
        """
        Search on Google
        query: search query
        """
        try:
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            return self.open_url(search_url)
        except Exception as e:
            logger.error(f"Error searching Google: {str(e)}")
            return False
    
    def search_youtube(self, query):
        """
        Search on YouTube
        query: search query
        """
        try:
            search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            return self.open_url(search_url)
        except Exception as e:
            logger.error(f"Error searching YouTube: {str(e)}")
            return False
    
    def open_website(self, site_name):
        """
        Open common websites by name
        site_name: name of website (e.g., 'youtube', 'gmail', 'github')
        """
        sites = {
            'youtube': 'https://youtube.com',
            'gmail': 'https://gmail.com',
            'github': 'https://github.com',
            'reddit': 'https://reddit.com',
            'twitter': 'https://twitter.com',
            'facebook': 'https://facebook.com',
            'instagram': 'https://instagram.com',
            'linkedin': 'https://linkedin.com',
            'stackoverflow': 'https://stackoverflow.com',
            'wikipedia': 'https://wikipedia.org',
            'amazon': 'https://amazon.com',
            'netflix': 'https://netflix.com',
            'spotify': 'https://spotify.com',
            'twitch': 'https://twitch.tv',
            'discord': 'https://discord.com',
        }
        
        site_name_lower = site_name.lower()
        
        if site_name_lower in sites:
            return self.open_url(sites[site_name_lower])
        else:
            # Try to open as domain
            return self.open_url(f"https://{site_name}.com")
    
    def close_tab(self):
        """Close current browser tab using Ctrl+W"""
        try:
            logger.info("Closing browser tab")
            pyautogui.hotkey('ctrl', 'w')
            return True
        except Exception as e:
            logger.error(f"Error closing tab: {str(e)}")
            return False
    
    def new_tab(self):
        """Open new browser tab using Ctrl+T"""
        try:
            logger.info("Opening new browser tab")
            pyautogui.hotkey('ctrl', 't')
            return True
        except Exception as e:
            logger.error(f"Error opening new tab: {str(e)}")
            return False
    
    def refresh_page(self):
        """Refresh current page using F5"""
        try:
            logger.info("Refreshing page")
            pyautogui.press('f5')
            return True
        except Exception as e:
            logger.error(f"Error refreshing page: {str(e)}")
            return False
    
    def go_back(self):
        """Go back in browser history using Alt+Left"""
        try:
            logger.info("Going back")
            pyautogui.hotkey('alt', 'left')
            return True
        except Exception as e:
            logger.error(f"Error going back: {str(e)}")
            return False
    
    def go_forward(self):
        """Go forward in browser history using Alt+Right"""
        try:
            logger.info("Going forward")
            pyautogui.hotkey('alt', 'right')
            return True
        except Exception as e:
            logger.error(f"Error going forward: {str(e)}")
            return False
    
    def zoom_in(self):
        """Zoom in using Ctrl++"""
        try:
            logger.info("Zooming in")
            pyautogui.hotkey('ctrl', '+')
            return True
        except Exception as e:
            logger.error(f"Error zooming in: {str(e)}")
            return False
    
    def zoom_out(self):
        """Zoom out using Ctrl+-"""
        try:
            logger.info("Zooming out")
            pyautogui.hotkey('ctrl', '-')
            return True
        except Exception as e:
            logger.error(f"Error zooming out: {str(e)}")
            return False
    
    def reset_zoom(self):
        """Reset zoom to 100% using Ctrl+0"""
        try:
            logger.info("Resetting zoom")
            pyautogui.hotkey('ctrl', '0')
            return True
        except Exception as e:
            logger.error(f"Error resetting zoom: {str(e)}")
            return False
    
    def focus_address_bar(self):
        """Focus browser address bar using Ctrl+L"""
        try:
            logger.info("Focusing address bar")
            pyautogui.hotkey('ctrl', 'l')
            return True
        except Exception as e:
            logger.error(f"Error focusing address bar: {str(e)}")
            return False
    
    def open_downloads(self):
        """Open downloads page using Ctrl+J"""
        try:
            logger.info("Opening downloads")
            pyautogui.hotkey('ctrl', 'j')
            return True
        except Exception as e:
            logger.error(f"Error opening downloads: {str(e)}")
            return False
    
    def open_history(self):
        """Open history page using Ctrl+H"""
        try:
            logger.info("Opening history")
            pyautogui.hotkey('ctrl', 'h')
            return True
        except Exception as e:
            logger.error(f"Error opening history: {str(e)}")
            return False
    
    def open_bookmarks(self):
        """Open bookmarks using Ctrl+Shift+B"""
        try:
            logger.info("Opening bookmarks")
            pyautogui.hotkey('ctrl', 'shift', 'b')
            return True
        except Exception as e:
            logger.error(f"Error opening bookmarks: {str(e)}")
            return False
    
    def find_in_page(self, text=None):
        """
        Open find in page dialog using Ctrl+F
        text: optional text to search for
        """
        try:
            logger.info("Opening find in page")
            pyautogui.hotkey('ctrl', 'f')
            
            if text:
                time.sleep(0.2)
                pyautogui.write(text)
            
            return True
        except Exception as e:
            logger.error(f"Error finding in page: {str(e)}")
            return False
    
    def scroll_page(self, direction='down', amount=3):
        """
        Scroll page
        direction: 'up' or 'down'
        amount: number of scroll clicks
        """
        try:
            logger.info(f"Scrolling {direction}")
            
            if direction == 'down':
                pyautogui.scroll(-amount)
            else:
                pyautogui.scroll(amount)
            
            return True
        except Exception as e:
            logger.error(f"Error scrolling: {str(e)}")
            return False
    
    def scroll_to_top(self):
        """Scroll to top of page using Home key"""
        try:
            logger.info("Scrolling to top")
            pyautogui.press('home')
            return True
        except Exception as e:
            logger.error(f"Error scrolling to top: {str(e)}")
            return False
    
    def scroll_to_bottom(self):
        """Scroll to bottom of page using End key"""
        try:
            logger.info("Scrolling to bottom")
            pyautogui.press('end')
            return True
        except Exception as e:
            logger.error(f"Error scrolling to bottom: {str(e)}")
            return False


if __name__ == "__main__":
    # Test browser controller
    browser = BrowserController()
    
    print("Testing browser controller...")
    
    # Open YouTube
    print("\nOpening YouTube...")
    browser.open_website('youtube')
    
    time.sleep(2)
    
    # Search Google
    print("\nSearching Google...")
    browser.search_google('Python programming')
    
    print("\nDone!")
