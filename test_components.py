"""
Test script to verify all Zox AI components
Run this before starting the main application
"""

import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_imports():
    """Test if all required modules can be imported"""
    print("=" * 50)
    print("Testing imports...")
    print("=" * 50)
    
    modules = {
        'PyQt6': 'GUI framework',
        'requests': 'HTTP requests',
        'pyautogui': 'Mouse/keyboard control',
        'psutil': 'System information',
        'pyttsx3': 'Text-to-speech',
    }
    
    optional_modules = {
        'faster_whisper': 'Speech-to-text',
        'pywinauto': 'Window automation',
        'pycaw': 'Volume control',
        'screen_brightness_control': 'Brightness control',
        'PIL': 'Screenshots',
        'schedule': 'Task scheduling',
    }
    
    all_ok = True
    
    # Test required modules
    for module, description in modules.items():
        try:
            __import__(module)
            print(f"✓ {module:30} - {description}")
        except ImportError:
            print(f"✗ {module:30} - {description} (REQUIRED)")
            all_ok = False
    
    print()
    
    # Test optional modules
    for module, description in optional_modules.items():
        try:
            __import__(module)
            print(f"✓ {module:30} - {description}")
        except ImportError:
            print(f"⚠ {module:30} - {description} (optional, some features disabled)")
    
    return all_ok


def test_ollama():
    """Test connection to Ollama"""
    print("\n" + "=" * 50)
    print("Testing Ollama connection...")
    print("=" * 50)
    
    try:
        from core.llm import LLMEngine
        
        llm = LLMEngine()
        
        if llm.test_connection():
            print("✓ Connected to Ollama successfully")
            
            # Test a simple query
            print("\nTesting LLM query...")
            result = llm.get_action_plan("What time is it?")
            
            if result:
                print(f"✓ LLM response received")
                print(f"  Response: {result.get('response', 'N/A')}")
                return True
            else:
                print("✗ LLM query failed")
                return False
        else:
            print("✗ Cannot connect to Ollama")
            print("  Make sure Ollama is running: ollama serve")
            print("  And the model is installed: ollama pull llama3.1:8b-instruct-q4_K_M")
            return False
            
    except Exception as e:
        print(f"✗ Error testing Ollama: {str(e)}")
        return False


def test_voice_output():
    """Test voice output"""
    print("\n" + "=" * 50)
    print("Testing voice output...")
    print("=" * 50)
    
    try:
        from core.voice_output import VoiceOutput
        
        voice = VoiceOutput()
        
        # List available voices
        voices = voice.list_voices()
        print(f"✓ Found {len(voices)} voice(s)")
        for idx, name, voice_id in voices:
            print(f"  {idx}: {name}")
        
        # Test speech
        print("\nTesting speech (you should hear this)...")
        voice.speak("Hello! I am Zox AI. Voice output is working.", blocking=True)
        print("✓ Voice output test complete")
        
        return True
        
    except Exception as e:
        print(f"✗ Error testing voice output: {str(e)}")
        return False


def test_system_info():
    """Test system information"""
    print("\n" + "=" * 50)
    print("Testing system information...")
    print("=" * 50)
    
    try:
        from actions.system_control import SystemController
        
        controller = SystemController()
        
        info = controller.get_system_info()
        
        print(f"✓ CPU Usage: {info.get('cpu', 'N/A')}%")
        print(f"✓ RAM Usage: {info.get('ram', 'N/A')}% ({info.get('ram_used_gb', 0):.1f} GB / {info.get('ram_total_gb', 0):.1f} GB)")
        print(f"✓ Disk Usage: {info.get('disk', 'N/A')}%")
        
        # Check RAM usage
        ram_used = info.get('ram_used_gb', 0)
        if ram_used > 7:
            print(f"⚠ Warning: RAM usage ({ram_used:.1f} GB) is above 7 GB target")
        
        return True
        
    except Exception as e:
        print(f"✗ Error testing system info: {str(e)}")
        return False


def test_file_operations():
    """Test file operations"""
    print("\n" + "=" * 50)
    print("Testing file operations...")
    print("=" * 50)
    
    try:
        from actions.file_control import FileController
        
        controller = FileController()
        
        # Create test file
        test_content = "This is a test file created by Zox AI"
        path = controller.create_file("test_zoxai.txt", test_content)
        print(f"✓ Created test file: {path}")
        
        # Read test file
        content = controller.read_file("test_zoxai.txt")
        assert content == test_content
        print(f"✓ Read test file successfully")
        
        # Delete test file
        controller.delete_file("test_zoxai.txt")
        print(f"✓ Deleted test file")
        
        return True
        
    except Exception as e:
        print(f"✗ Error testing file operations: {str(e)}")
        return False


def test_app_control():
    """Test app control"""
    print("\n" + "=" * 50)
    print("Testing app control...")
    print("=" * 50)
    
    try:
        from actions.app_control import AppController
        
        controller = AppController()
        
        # List running apps
        apps = controller.list_running_apps()
        print(f"✓ Found {len(apps)} running processes")
        
        # Show first 5
        print("  Sample processes:")
        for name, pid in apps[:5]:
            print(f"    {name} (PID: {pid})")
        
        return True
        
    except Exception as e:
        print(f"✗ Error testing app control: {str(e)}")
        return False


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 48 + "╗")
    print("║" + " " * 10 + "Zox AI Component Test Suite" + " " * 11 + "║")
    print("║" + " " * 15 + "by MrLexCoder" + " " * 20 + "║")
    print("╚" + "=" * 48 + "╝")
    print()
    
    results = {
        'Imports': test_imports(),
        'Ollama': test_ollama(),
        'Voice Output': test_voice_output(),
        'System Info': test_system_info(),
        'File Operations': test_file_operations(),
        'App Control': test_app_control(),
    }
    
    # Summary
    print("\n" + "=" * 50)
    print("Test Summary")
    print("=" * 50)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name:20} {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✓ All tests passed! Zox AI is ready to run.")
        print("\nRun: python main.py")
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  - Install missing packages: pip install -r requirements.txt")
        print("  - Start Ollama: ollama serve")
        print("  - Pull model: ollama pull llama3.1:8b-instruct-q4_K_M")
    print("=" * 50)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
