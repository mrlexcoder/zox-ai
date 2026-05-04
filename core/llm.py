"""
LLM Engine - Ollama API interface
Communicates with Llama 3.1 8B model running locally
"""

import requests
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LLMEngine:
    """Interface to Ollama LLM for command understanding and action planning"""
    
    def __init__(self, base_url="http://localhost:11434", model="llama3.1:8b-instruct-q4_K_M"):
        self.base_url = base_url
        self.model = model
        self.api_url = f"{base_url}/api/generate"
        
        # System prompt for Zox AI
        self.system_prompt = """You are Zox AI, an AI desktop assistant. Your job is to understand user commands and create action plans.

You must respond ONLY with valid JSON in this exact format:
{
    "response": "A friendly response to the user",
    "actions": [
        {
            "intent": "action_type",
            "param1": "value1",
            "param2": "value2"
        }
    ]
}

Available intents and their parameters:

1. open_app: {"intent": "open_app", "app": "chrome|notepad|calculator|explorer|etc"}
2. close_app: {"intent": "close_app", "app": "app_name"}
3. create_file: {"intent": "create_file", "path": "file_path", "content": "file_content"}
4. delete_file: {"intent": "delete_file", "path": "file_path"}
5. read_file: {"intent": "read_file", "path": "file_path"}
6. type_text: {"intent": "type_text", "text": "text_to_type", "interval": 0.05}
7. move_mouse: {"intent": "move_mouse", "x": 100, "y": 200}
8. click_mouse: {"intent": "click_mouse", "button": "left|right|middle"}
9. press_key: {"intent": "press_key", "key": "enter|space|tab|etc"}
10. open_url: {"intent": "open_url", "url": "https://example.com"}
11. screenshot: {"intent": "screenshot", "path": "screenshot.png"}
12. set_volume: {"intent": "set_volume", "level": 50}
13. set_brightness: {"intent": "set_brightness", "level": 75}
14. get_system_info: {"intent": "get_system_info"}
15. schedule_task: {"intent": "schedule_task", "time": "14:30", "command": "task_description"}

Examples:

User: "Open Chrome and go to YouTube"
Response:
{
    "response": "Opening Chrome and navigating to YouTube",
    "actions": [
        {"intent": "open_app", "app": "chrome"},
        {"intent": "open_url", "url": "https://youtube.com"}
    ]
}

User: "Create a file called test.txt with hello world"
Response:
{
    "response": "Creating test.txt with your content",
    "actions": [
        {"intent": "create_file", "path": "test.txt", "content": "hello world"}
    ]
}

User: "What's my CPU usage?"
Response:
{
    "response": "Let me check your system information",
    "actions": [
        {"intent": "get_system_info"}
    ]
}

User: "Type 'Hello World' slowly"
Response:
{
    "response": "Typing 'Hello World' with human-like speed",
    "actions": [
        {"intent": "type_text", "text": "Hello World", "interval": 0.1}
    ]
}

IMPORTANT: Always respond with valid JSON only. No extra text before or after."""

    def get_action_plan(self, user_input):
        """
        Get action plan from LLM based on user input
        Returns: dict with 'response' and 'actions' keys
        """
        try:
            # Construct the full prompt
            full_prompt = f"{self.system_prompt}\n\nUser: {user_input}\nResponse:"
            
            # Make request to Ollama
            payload = {
                "model": self.model,
                "prompt": full_prompt,
                "stream": False,
                "temperature": 0.3,  # Lower temperature for more consistent JSON
                "top_p": 0.9,
                "max_tokens": 500
            }
            
            logger.info(f"Sending request to Ollama: {user_input}")
            
            response = requests.post(
                self.api_url,
                json=payload,
                timeout=30
            )
            
            if response.status_code != 200:
                logger.error(f"Ollama API error: {response.status_code}")
                return self._fallback_response(user_input)
            
            # Parse response
            result = response.json()
            llm_response = result.get("response", "")
            
            logger.info(f"LLM raw response: {llm_response}")
            
            # Extract JSON from response
            action_plan = self._extract_json(llm_response)
            
            if action_plan:
                return action_plan
            else:
                return self._fallback_response(user_input)
                
        except requests.exceptions.ConnectionError:
            logger.error("Cannot connect to Ollama. Is it running?")
            return {
                "response": "I can't connect to my AI brain. Please make sure Ollama is running with: ollama serve",
                "actions": []
            }
        except Exception as e:
            logger.error(f"Error getting action plan: {str(e)}")
            return self._fallback_response(user_input)
    
    def _extract_json(self, text):
        """Extract JSON from LLM response"""
        try:
            # Try to parse directly
            return json.loads(text)
        except json.JSONDecodeError:
            # Try to find JSON in text
            start = text.find('{')
            end = text.rfind('}') + 1
            
            if start != -1 and end > start:
                try:
                    json_str = text[start:end]
                    return json.loads(json_str)
                except json.JSONDecodeError:
                    pass
            
            return None
    
    def _fallback_response(self, user_input):
        """Fallback response when LLM fails"""
        # Simple keyword-based fallback
        user_lower = user_input.lower()
        
        if "open" in user_lower and "chrome" in user_lower:
            return {
                "response": "Opening Chrome",
                "actions": [{"intent": "open_app", "app": "chrome"}]
            }
        elif "open" in user_lower and "notepad" in user_lower:
            return {
                "response": "Opening Notepad",
                "actions": [{"intent": "open_app", "app": "notepad"}]
            }
        elif "screenshot" in user_lower:
            return {
                "response": "Taking a screenshot",
                "actions": [{"intent": "screenshot", "path": "screenshot.png"}]
            }
        elif "system" in user_lower or "cpu" in user_lower or "ram" in user_lower:
            return {
                "response": "Checking system information",
                "actions": [{"intent": "get_system_info"}]
            }
        else:
            return {
                "response": "I'm not sure how to help with that. Could you rephrase?",
                "actions": []
            }
    
    def test_connection(self):
        """Test connection to Ollama"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False


if __name__ == "__main__":
    # Test the LLM engine
    llm = LLMEngine()
    
    if llm.test_connection():
        print("✓ Connected to Ollama")
        
        # Test command
        result = llm.get_action_plan("Open Chrome and go to YouTube")
        print(f"\nTest result: {json.dumps(result, indent=2)}")
    else:
        print("✗ Cannot connect to Ollama. Make sure it's running!")
