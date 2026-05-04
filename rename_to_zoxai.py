"""
Script to rename JARVIS to Zox AI throughout the project
"""

import os
import re
from pathlib import Path

def replace_in_file(file_path, replacements):
    """Replace text in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated: {file_path}")
            return True
        return False
    except Exception as e:
        print(f"✗ Error updating {file_path}: {e}")
        return False

def main():
    # Define replacements
    replacements = {
        'JARVIS': 'Zox AI',
        'Jarvis': 'Zox AI',
        'jarvis': 'zoxai',
        'JarvisGUI': 'ZoxAIGUI',
        'JARVIS_Screenshots': 'ZoxAI_Screenshots',
        'JARVIS/': 'ZoxAI/',
    }
    
    # File extensions to process
    extensions = ['.py', '.md', '.txt', '.bat', '.json', '.example']
    
    # Get all files
    files_to_process = []
    for ext in extensions:
        files_to_process.extend(Path('.').rglob(f'*{ext}'))
    
    # Exclude this script and git folder
    files_to_process = [f for f in files_to_process if 'rename_to_zoxai.py' not in str(f) and '.git' not in str(f)]
    
    print(f"Found {len(files_to_process)} files to process\n")
    
    updated_count = 0
    for file_path in files_to_process:
        if replace_in_file(file_path, replacements):
            updated_count += 1
    
    print(f"\n✓ Updated {updated_count} files")
    print("✓ Renaming complete!")

if __name__ == "__main__":
    main()
