"""
System Control - Volume, brightness, screenshots, system info
Uses psutil, pycaw, screen-brightness-control, and PIL
"""

import psutil
import logging
import subprocess
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import optional dependencies
try:
    from PIL import ImageGrab
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    logger.warning("PIL not available. Screenshot functionality limited.")

try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    from comtypes import CLSCTX_ALL
    PYCAW_AVAILABLE = True
except ImportError:
    PYCAW_AVAILABLE = False
    logger.warning("pycaw not available. Volume control disabled.")

try:
    import screen_brightness_control as sbc
    SBC_AVAILABLE = True
except ImportError:
    SBC_AVAILABLE = False
    logger.warning("screen-brightness-control not available. Brightness control disabled.")


class SystemController:
    """Control system settings and get system information"""
    
    def __init__(self):
        self.screenshot_dir = Path.home() / "Pictures" / "Zox AI_Screenshots"
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize volume control
        self.volume_interface = None
        if PYCAW_AVAILABLE:
            try:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                self.volume_interface = interface.QueryInterface(IAudioEndpointVolume)
                logger.info("Volume control initialized")
            except Exception as e:
                logger.error(f"Failed to initialize volume control: {str(e)}")
    
    # ===== SYSTEM INFORMATION =====
    
    def get_system_info(self):
        """
        Get system information (CPU, RAM, disk usage)
        Returns: dict with system info
        """
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            info = {
                'cpu': cpu_percent,
                'ram': memory.percent,
                'ram_used_gb': memory.used / (1024**3),
                'ram_total_gb': memory.total / (1024**3),
                'disk': disk.percent,
                'disk_used_gb': disk.used / (1024**3),
                'disk_total_gb': disk.total / (1024**3)
            }
            
            logger.info(f"System info: CPU {cpu_percent}%, RAM {memory.percent}%, Disk {disk.percent}%")
            return info
            
        except Exception as e:
            logger.error(f"Error getting system info: {str(e)}")
            return {}
    
    def get_cpu_info(self):
        """Get detailed CPU information"""
        try:
            cpu_freq = psutil.cpu_freq()
            cpu_count = psutil.cpu_count()
            cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
            
            return {
                'count': cpu_count,
                'frequency_mhz': cpu_freq.current if cpu_freq else None,
                'percent_total': psutil.cpu_percent(interval=1),
                'percent_per_core': cpu_percent_per_core
            }
        except Exception as e:
            logger.error(f"Error getting CPU info: {str(e)}")
            return {}
    
    def get_memory_info(self):
        """Get detailed memory information"""
        try:
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            return {
                'total_gb': memory.total / (1024**3),
                'available_gb': memory.available / (1024**3),
                'used_gb': memory.used / (1024**3),
                'percent': memory.percent,
                'swap_total_gb': swap.total / (1024**3),
                'swap_used_gb': swap.used / (1024**3),
                'swap_percent': swap.percent
            }
        except Exception as e:
            logger.error(f"Error getting memory info: {str(e)}")
            return {}
    
    def get_disk_info(self):
        """Get disk information for all partitions"""
        try:
            partitions = psutil.disk_partitions()
            disk_info = []
            
            for partition in partitions:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disk_info.append({
                        'device': partition.device,
                        'mountpoint': partition.mountpoint,
                        'fstype': partition.fstype,
                        'total_gb': usage.total / (1024**3),
                        'used_gb': usage.used / (1024**3),
                        'free_gb': usage.free / (1024**3),
                        'percent': usage.percent
                    })
                except PermissionError:
                    pass
            
            return disk_info
        except Exception as e:
            logger.error(f"Error getting disk info: {str(e)}")
            return []
    
    def get_battery_info(self):
        """Get battery information (for laptops)"""
        try:
            battery = psutil.sensors_battery()
            
            if battery:
                return {
                    'percent': battery.percent,
                    'plugged_in': battery.power_plugged,
                    'time_left_minutes': battery.secsleft / 60 if battery.secsleft != psutil.POWER_TIME_UNLIMITED else None
                }
            else:
                return {'error': 'No battery detected'}
        except Exception as e:
            logger.error(f"Error getting battery info: {str(e)}")
            return {}
    
    def get_network_info(self):
        """Get network information"""
        try:
            net_io = psutil.net_io_counters()
            
            return {
                'bytes_sent_mb': net_io.bytes_sent / (1024**2),
                'bytes_recv_mb': net_io.bytes_recv / (1024**2),
                'packets_sent': net_io.packets_sent,
                'packets_recv': net_io.packets_recv
            }
        except Exception as e:
            logger.error(f"Error getting network info: {str(e)}")
            return {}
    
    # ===== VOLUME CONTROL =====
    
    def get_volume(self):
        """
        Get current volume level
        Returns: volume level (0-100) or None
        """
        if not self.volume_interface:
            logger.error("Volume control not available")
            return None
        
        try:
            current_volume = self.volume_interface.GetMasterVolumeLevelScalar()
            volume_percent = int(current_volume * 100)
            logger.info(f"Current volume: {volume_percent}%")
            return volume_percent
        except Exception as e:
            logger.error(f"Error getting volume: {str(e)}")
            return None
    
    def set_volume(self, level):
        """
        Set volume level
        level: volume level (0-100)
        """
        if not self.volume_interface:
            logger.error("Volume control not available")
            return False
        
        try:
            level = max(0, min(100, level))  # Clamp to 0-100
            volume_scalar = level / 100.0
            
            self.volume_interface.SetMasterVolumeLevelScalar(volume_scalar, None)
            logger.info(f"Set volume to {level}%")
            return True
        except Exception as e:
            logger.error(f"Error setting volume: {str(e)}")
            return False
    
    def mute(self):
        """Mute audio"""
        if not self.volume_interface:
            logger.error("Volume control not available")
            return False
        
        try:
            self.volume_interface.SetMute(1, None)
            logger.info("Muted audio")
            return True
        except Exception as e:
            logger.error(f"Error muting: {str(e)}")
            return False
    
    def unmute(self):
        """Unmute audio"""
        if not self.volume_interface:
            logger.error("Volume control not available")
            return False
        
        try:
            self.volume_interface.SetMute(0, None)
            logger.info("Unmuted audio")
            return True
        except Exception as e:
            logger.error(f"Error unmuting: {str(e)}")
            return False
    
    # ===== BRIGHTNESS CONTROL =====
    
    def get_brightness(self):
        """
        Get current brightness level
        Returns: brightness level (0-100) or None
        """
        if not SBC_AVAILABLE:
            logger.error("Brightness control not available")
            return None
        
        try:
            brightness = sbc.get_brightness()
            if isinstance(brightness, list):
                brightness = brightness[0]
            logger.info(f"Current brightness: {brightness}%")
            return brightness
        except Exception as e:
            logger.error(f"Error getting brightness: {str(e)}")
            return None
    
    def set_brightness(self, level):
        """
        Set brightness level
        level: brightness level (0-100)
        """
        if not SBC_AVAILABLE:
            logger.error("Brightness control not available")
            return False
        
        try:
            level = max(0, min(100, level))  # Clamp to 0-100
            sbc.set_brightness(level)
            logger.info(f"Set brightness to {level}%")
            return True
        except Exception as e:
            logger.error(f"Error setting brightness: {str(e)}")
            return False
    
    # ===== SCREENSHOT =====
    
    def take_screenshot(self, path=None):
        """
        Take a screenshot
        path: optional path to save screenshot (defaults to Pictures/Zox AI_Screenshots)
        Returns: path to saved screenshot
        """
        if not PIL_AVAILABLE:
            logger.error("PIL not available for screenshots")
            return None
        
        try:
            # Generate filename if not provided
            if path is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                path = self.screenshot_dir / f"screenshot_{timestamp}.png"
            else:
                path = Path(path)
            
            # Take screenshot
            screenshot = ImageGrab.grab()
            screenshot.save(path)
            
            logger.info(f"Screenshot saved to {path}")
            return str(path)
            
        except Exception as e:
            logger.error(f"Error taking screenshot: {str(e)}")
            return None
    
    # ===== POWER MANAGEMENT =====
    
    def shutdown(self, delay_seconds=0):
        """
        Shutdown the computer
        delay_seconds: delay before shutdown
        """
        try:
            logger.warning(f"Shutting down in {delay_seconds} seconds")
            subprocess.run(['shutdown', '/s', '/t', str(delay_seconds)])
            return True
        except Exception as e:
            logger.error(f"Error shutting down: {str(e)}")
            return False
    
    def restart(self, delay_seconds=0):
        """
        Restart the computer
        delay_seconds: delay before restart
        """
        try:
            logger.warning(f"Restarting in {delay_seconds} seconds")
            subprocess.run(['shutdown', '/r', '/t', str(delay_seconds)])
            return True
        except Exception as e:
            logger.error(f"Error restarting: {str(e)}")
            return False
    
    def sleep(self):
        """Put computer to sleep"""
        try:
            logger.info("Putting computer to sleep")
            subprocess.run(['rundll32.exe', 'powrprof.dll,SetSuspendState', '0,1,0'])
            return True
        except Exception as e:
            logger.error(f"Error sleeping: {str(e)}")
            return False
    
    def lock_screen(self):
        """Lock the screen"""
        try:
            logger.info("Locking screen")
            subprocess.run(['rundll32.exe', 'user32.dll,LockWorkStation'])
            return True
        except Exception as e:
            logger.error(f"Error locking screen: {str(e)}")
            return False


if __name__ == "__main__":
    # Test system controller
    controller = SystemController()
    
    print("Testing system controller...")
    
    # Get system info
    print("\nSystem Info:")
    info = controller.get_system_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # Get volume
    print(f"\nCurrent volume: {controller.get_volume()}%")
    
    # Get brightness
    print(f"Current brightness: {controller.get_brightness()}%")
    
    # Take screenshot
    print("\nTaking screenshot...")
    path = controller.take_screenshot()
    print(f"Screenshot saved to: {path}")
    
    print("\nDone!")
