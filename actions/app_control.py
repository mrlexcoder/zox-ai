"""
App Control - Open, close, and manage applications
Uses subprocess and pywinauto
"""

import subprocess
import logging
import time
import psutil
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from pywinauto import Application
    PYWINAUTO_AVAILABLE = True
except ImportError:
    PYWINAUTO_AVAILABLE = False
    logger.warning("pywinauto not available. Some features may be limited.")


class AppController:
    """Control Windows applications"""
    
    def __init__(self):
        # Common Windows applications and their executables
        self.app_map = {
            "chrome": "chrome.exe",
            "firefox": "firefox.exe",
            "edge": "msedge.exe",
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "explorer": "explorer.exe",
            "cmd": "cmd.exe",
            "powershell": "powershell.exe",
            "paint": "mspaint.exe",
            "wordpad": "write.exe",
            "task manager": "taskmgr.exe",
            "control panel": "control.exe",
            "settings": "ms-settings:",
            "vscode": "code.exe",
            "spotify": "spotify.exe",
            "discord": "discord.exe",
            "slack": "slack.exe",
            "teams": "teams.exe",
            "outlook": "outlook.exe",
            "excel": "excel.exe",
            "word": "winword.exe",
            "powerpoint": "powerpnt.exe",
        }
    
    def open_app(self, app_name):
        """
        Open an application
        app_name: name of the app (e.g., 'chrome', 'notepad')
        """
        try:
            app_name_lower = app_name.lower()
            
            # Get executable name
            if app_name_lower in self.app_map:
                executable = self.app_map[app_name_lower]
            else:
                # Try to use the name directly
                executable = app_name if app_name.endswith('.exe') else f"{app_name}.exe"
            
            logger.info(f"Opening {app_name} ({executable})")
            
            # Special handling for Windows settings
            if executable.startswith("ms-settings:"):
                os.system(f'start {executable}')
                return True
            
            # Try to launch the application
            try:
                subprocess.Popen(executable, shell=True)
                logger.info(f"Successfully opened {app_name}")
                return True
            except FileNotFoundError:
                # Try common installation paths
                common_paths = [
                    f"C:\\Program Files\\{app_name}\\{executable}",
                    f"C:\\Program Files (x86)\\{app_name}\\{executable}",
                    f"{os.environ.get('LOCALAPPDATA')}\\Programs\\{app_name}\\{executable}",
                ]
                
                for path in common_paths:
                    if os.path.exists(path):
                        subprocess.Popen(path)
                        logger.info(f"Successfully opened {app_name} from {path}")
                        return True
                
                logger.error(f"Could not find {app_name}")
                return False
                
        except Exception as e:
            logger.error(f"Error opening {app_name}: {str(e)}")
            return False
    
    def close_app(self, app_name):
        """
        Close an application by name
        app_name: name of the app to close
        """
        try:
            app_name_lower = app_name.lower()
            
            # Get executable name
            if app_name_lower in self.app_map:
                executable = self.app_map[app_name_lower]
            else:
                executable = app_name if app_name.endswith('.exe') else f"{app_name}.exe"
            
            logger.info(f"Closing {app_name} ({executable})")
            
            # Find and terminate the process
            closed = False
            for proc in psutil.process_iter(['name', 'pid']):
                try:
                    if proc.info['name'].lower() == executable.lower():
                        proc.terminate()
                        closed = True
                        logger.info(f"Terminated {app_name} (PID: {proc.info['pid']})")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            if closed:
                return True
            else:
                logger.warning(f"{app_name} is not running")
                return False
                
        except Exception as e:
            logger.error(f"Error closing {app_name}: {str(e)}")
            return False
    
    def is_app_running(self, app_name):
        """
        Check if an application is running
        Returns: True if running, False otherwise
        """
        try:
            app_name_lower = app_name.lower()
            
            if app_name_lower in self.app_map:
                executable = self.app_map[app_name_lower]
            else:
                executable = app_name if app_name.endswith('.exe') else f"{app_name}.exe"
            
            for proc in psutil.process_iter(['name']):
                try:
                    if proc.info['name'].lower() == executable.lower():
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            return False
            
        except Exception as e:
            logger.error(f"Error checking if {app_name} is running: {str(e)}")
            return False
    
    def list_running_apps(self):
        """
        List all running applications
        Returns: list of (name, pid) tuples
        """
        try:
            apps = []
            for proc in psutil.process_iter(['name', 'pid']):
                try:
                    apps.append((proc.info['name'], proc.info['pid']))
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            return apps
        except Exception as e:
            logger.error(f"Error listing running apps: {str(e)}")
            return []
    
    def focus_app(self, app_name):
        """
        Bring an application window to focus
        Requires pywinauto
        """
        if not PYWINAUTO_AVAILABLE:
            logger.error("pywinauto not available")
            return False
        
        try:
            app_name_lower = app_name.lower()
            
            if app_name_lower in self.app_map:
                executable = self.app_map[app_name_lower]
            else:
                executable = app_name
            
            # Try to connect to the application
            app = Application().connect(path=executable, timeout=5)
            
            # Get the main window and set focus
            window = app.top_window()
            window.set_focus()
            
            logger.info(f"Focused {app_name}")
            return True
            
        except Exception as e:
            logger.error(f"Error focusing {app_name}: {str(e)}")
            return False
    
    def get_window_title(self, app_name):
        """
        Get the title of an application's main window
        Requires pywinauto
        """
        if not PYWINAUTO_AVAILABLE:
            logger.error("pywinauto not available")
            return None
        
        try:
            app_name_lower = app_name.lower()
            
            if app_name_lower in self.app_map:
                executable = self.app_map[app_name_lower]
            else:
                executable = app_name
            
            app = Application().connect(path=executable, timeout=5)
            window = app.top_window()
            
            return window.window_text()
            
        except Exception as e:
            logger.error(f"Error getting window title for {app_name}: {str(e)}")
            return None


if __name__ == "__main__":
    # Test app controller
    controller = AppController()
    
    print("Testing app controller...")
    
    # Open notepad
    print("\nOpening Notepad...")
    controller.open_app("notepad")
    time.sleep(2)
    
    # Check if running
    print(f"Notepad running: {controller.is_app_running('notepad')}")
    
    # List running apps
    print("\nRunning apps (first 10):")
    for name, pid in controller.list_running_apps()[:10]:
        print(f"  {name} (PID: {pid})")
    
    # Close notepad
    print("\nClosing Notepad...")
    controller.close_app("notepad")
    time.sleep(1)
    
    print(f"Notepad running: {controller.is_app_running('notepad')}")
