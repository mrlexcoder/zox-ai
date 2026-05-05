"""
Notification Control - Windows notifications
"""

import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from win10toast import ToastNotifier
    TOAST_AVAILABLE = True
except ImportError:
    TOAST_AVAILABLE = False
    logger.warning("win10toast not available. Notifications will be limited.")


class NotificationController:
    """Control Windows notifications"""
    
    def __init__(self):
        if TOAST_AVAILABLE:
            self.toaster = ToastNotifier()
            logger.info("Notification controller initialized")
        else:
            self.toaster = None
            logger.warning("Notification controller running in fallback mode")
    
    def show_notification(self, title, message, duration=5, icon_path=None):
        """
        Show a Windows notification
        title: notification title
        message: notification message
        duration: duration in seconds
        icon_path: path to icon file (optional)
        """
        try:
            if self.toaster:
                self.toaster.show_toast(
                    title,
                    message,
                    duration=duration,
                    icon_path=icon_path,
                    threaded=True
                )
                logger.info(f"Notification shown: {title}")
                return True
            else:
                # Fallback: print to console
                print(f"\n[NOTIFICATION] {title}")
                print(f"  {message}\n")
                return True
        except Exception as e:
            logger.error(f"Error showing notification: {str(e)}")
            return False
    
    def show_success(self, message):
        """Show success notification"""
        return self.show_notification("✅ Success", message, duration=3)
    
    def show_error(self, message):
        """Show error notification"""
        return self.show_notification("❌ Error", message, duration=5)
    
    def show_info(self, message):
        """Show info notification"""
        return self.show_notification("ℹ️ Info", message, duration=4)
    
    def show_warning(self, message):
        """Show warning notification"""
        return self.show_notification("⚠️ Warning", message, duration=4)
    
    def show_reminder(self, message):
        """Show reminder notification"""
        timestamp = datetime.now().strftime("%H:%M")
        return self.show_notification(
            f"⏰ Reminder ({timestamp})",
            message,
            duration=10
        )


if __name__ == "__main__":
    # Test notification controller
    notifier = NotificationController()
    
    print("Testing notifications...")
    
    notifier.show_notification("Zox AI", "Hello! I'm your AI assistant.")
    
    import time
    time.sleep(2)
    
    notifier.show_success("Task completed successfully!")
    time.sleep(2)
    
    notifier.show_info("System information updated")
    time.sleep(2)
    
    notifier.show_warning("High CPU usage detected")
    time.sleep(2)
    
    notifier.show_reminder("Time for a break!")
    
    print("Done!")
