"""
Zox AI Banner and Version Info
"""

VERSION = "1.0.0"
AUTHOR = "MrLexCoder"

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███████╗ ██████╗ ██╗  ██╗     █████╗ ██╗                ║
║   ╚══███╔╝██╔═══██╗╚██╗██╔╝    ██╔══██╗██║                ║
║     ███╔╝ ██║   ██║ ╚███╔╝     ███████║██║                ║
║    ███╔╝  ██║   ██║ ██╔██╗     ██╔══██║██║                ║
║   ███████╗╚██████╔╝██╔╝ ██╗    ██║  ██║██║                ║
║   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝                ║
║                                                              ║
║              Your Offline AI Desktop Assistant               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

def print_banner():
    """Print the Zox AI banner"""
    print("\033[92m" + BANNER + "\033[0m")  # Green color
    print(f"\033[96m  Version: {VERSION} | Built by {AUTHOR}\033[0m")  # Cyan color
    print(f"\033[93m  🤖 Powered by Ollama + Llama 3.1 8B\033[0m")  # Yellow color
    print(f"\033[95m  🔒 100% Offline | 🎤 Voice Enabled | 🖥️ Full Control\033[0m\n")  # Magenta color

def get_version():
    """Get Zox AI version"""
    return VERSION

def get_author():
    """Get author name"""
    return AUTHOR
