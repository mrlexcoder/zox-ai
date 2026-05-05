"""
Command History and Favorites Manager
"""

import json
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HistoryManager:
    """Manage command history and favorites"""
    
    def __init__(self, history_file=None):
        if history_file is None:
            self.history_file = Path.home() / "Documents" / "ZoxAI" / "history.json"
        else:
            self.history_file = Path(history_file)
        
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        
        self.history = []
        self.favorites = []
        self.load_history()
    
    def load_history(self):
        """Load history from file"""
        try:
            if self.history_file.exists():
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.history = data.get('history', [])
                    self.favorites = data.get('favorites', [])
                logger.info(f"Loaded {len(self.history)} history items")
        except Exception as e:
            logger.error(f"Error loading history: {str(e)}")
    
    def save_history(self):
        """Save history to file"""
        try:
            data = {
                'history': self.history[-1000:],  # Keep last 1000 items
                'favorites': self.favorites
            }
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info("History saved")
        except Exception as e:
            logger.error(f"Error saving history: {str(e)}")
    
    def add_command(self, command, response=None, success=True):
        """
        Add command to history
        command: user command
        response: AI response
        success: whether command was successful
        """
        entry = {
            'timestamp': datetime.now().isoformat(),
            'command': command,
            'response': response,
            'success': success
        }
        self.history.append(entry)
        self.save_history()
        logger.info(f"Added to history: {command[:50]}...")
    
    def get_recent_commands(self, count=10):
        """Get recent commands"""
        return self.history[-count:]
    
    def search_history(self, query):
        """Search history for commands containing query"""
        results = []
        query_lower = query.lower()
        for entry in self.history:
            if query_lower in entry['command'].lower():
                results.append(entry)
        return results
    
    def add_favorite(self, command, description=None):
        """Add command to favorites"""
        favorite = {
            'command': command,
            'description': description or command,
            'added': datetime.now().isoformat()
        }
        
        # Check if already in favorites
        for fav in self.favorites:
            if fav['command'] == command:
                logger.info("Command already in favorites")
                return False
        
        self.favorites.append(favorite)
        self.save_history()
        logger.info(f"Added to favorites: {command}")
        return True
    
    def remove_favorite(self, command):
        """Remove command from favorites"""
        self.favorites = [f for f in self.favorites if f['command'] != command]
        self.save_history()
        logger.info(f"Removed from favorites: {command}")
    
    def get_favorites(self):
        """Get all favorite commands"""
        return self.favorites
    
    def clear_history(self):
        """Clear all history (keep favorites)"""
        self.history = []
        self.save_history()
        logger.info("History cleared")
    
    def get_statistics(self):
        """Get usage statistics"""
        total_commands = len(self.history)
        successful_commands = sum(1 for h in self.history if h.get('success', True))
        
        # Most used commands
        command_counts = {}
        for entry in self.history:
            cmd = entry['command'][:50]  # First 50 chars
            command_counts[cmd] = command_counts.get(cmd, 0) + 1
        
        most_used = sorted(command_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'total_commands': total_commands,
            'successful_commands': successful_commands,
            'success_rate': (successful_commands / total_commands * 100) if total_commands > 0 else 0,
            'favorites_count': len(self.favorites),
            'most_used': most_used
        }


if __name__ == "__main__":
    # Test history manager
    history = HistoryManager()
    
    print("Testing history manager...")
    
    # Add commands
    history.add_command("Open Chrome", "Opening Chrome", True)
    history.add_command("What's my CPU usage?", "CPU: 45%", True)
    history.add_command("Take a screenshot", "Screenshot saved", True)
    
    # Add favorites
    history.add_favorite("Open Chrome and go to YouTube", "Quick YouTube access")
    history.add_favorite("What's my system info?", "System status check")
    
    # Get recent
    print("\nRecent commands:")
    for cmd in history.get_recent_commands(5):
        print(f"  - {cmd['command']}")
    
    # Get favorites
    print("\nFavorites:")
    for fav in history.get_favorites():
        print(f"  - {fav['command']}")
    
    # Statistics
    print("\nStatistics:")
    stats = history.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\nDone!")
