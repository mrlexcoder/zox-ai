"""
File Control - Create, read, write, delete files and folders
"""

import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FileController:
    """Control file system operations"""
    
    def __init__(self, base_dir=None):
        """
        Initialize file controller
        base_dir: base directory for relative paths (defaults to user's Documents)
        """
        if base_dir is None:
            self.base_dir = Path.home() / "Documents" / "Zox AI"
            self.base_dir.mkdir(parents=True, exist_ok=True)
        else:
            self.base_dir = Path(base_dir)
    
    def _resolve_path(self, path):
        """Resolve path relative to base directory"""
        path = Path(path)
        if not path.is_absolute():
            path = self.base_dir / path
        return path
    
    def create_file(self, path, content=""):
        """
        Create a file with optional content
        path: file path (relative or absolute)
        content: file content
        """
        try:
            file_path = self._resolve_path(path)
            
            # Create parent directories if needed
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Created file: {file_path}")
            return str(file_path)
            
        except Exception as e:
            logger.error(f"Error creating file {path}: {str(e)}")
            raise
    
    def read_file(self, path):
        """
        Read file content
        path: file path (relative or absolute)
        Returns: file content as string
        """
        try:
            file_path = self._resolve_path(path)
            
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            logger.info(f"Read file: {file_path}")
            return content
            
        except Exception as e:
            logger.error(f"Error reading file {path}: {str(e)}")
            raise
    
    def write_file(self, path, content, append=False):
        """
        Write content to file
        path: file path (relative or absolute)
        content: content to write
        append: if True, append to file; if False, overwrite
        """
        try:
            file_path = self._resolve_path(path)
            
            # Create parent directories if needed
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            mode = 'a' if append else 'w'
            with open(file_path, mode, encoding='utf-8') as f:
                f.write(content)
            
            action = "Appended to" if append else "Wrote to"
            logger.info(f"{action} file: {file_path}")
            return str(file_path)
            
        except Exception as e:
            logger.error(f"Error writing to file {path}: {str(e)}")
            raise
    
    def delete_file(self, path):
        """
        Delete a file
        path: file path (relative or absolute)
        """
        try:
            file_path = self._resolve_path(path)
            
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            
            if file_path.is_file():
                file_path.unlink()
                logger.info(f"Deleted file: {file_path}")
            else:
                raise ValueError(f"Not a file: {file_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error deleting file {path}: {str(e)}")
            raise
    
    def create_folder(self, path):
        """
        Create a folder
        path: folder path (relative or absolute)
        """
        try:
            folder_path = self._resolve_path(path)
            folder_path.mkdir(parents=True, exist_ok=True)
            
            logger.info(f"Created folder: {folder_path}")
            return str(folder_path)
            
        except Exception as e:
            logger.error(f"Error creating folder {path}: {str(e)}")
            raise
    
    def delete_folder(self, path):
        """
        Delete a folder and its contents
        path: folder path (relative or absolute)
        """
        try:
            folder_path = self._resolve_path(path)
            
            if not folder_path.exists():
                raise FileNotFoundError(f"Folder not found: {folder_path}")
            
            if folder_path.is_dir():
                shutil.rmtree(folder_path)
                logger.info(f"Deleted folder: {folder_path}")
            else:
                raise ValueError(f"Not a folder: {folder_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error deleting folder {path}: {str(e)}")
            raise
    
    def list_files(self, path=".", pattern="*"):
        """
        List files in a directory
        path: directory path (relative or absolute)
        pattern: glob pattern (e.g., "*.txt")
        Returns: list of file paths
        """
        try:
            dir_path = self._resolve_path(path)
            
            if not dir_path.exists():
                raise FileNotFoundError(f"Directory not found: {dir_path}")
            
            if not dir_path.is_dir():
                raise ValueError(f"Not a directory: {dir_path}")
            
            files = [str(f) for f in dir_path.glob(pattern) if f.is_file()]
            
            logger.info(f"Listed {len(files)} files in {dir_path}")
            return files
            
        except Exception as e:
            logger.error(f"Error listing files in {path}: {str(e)}")
            raise
    
    def copy_file(self, src, dst):
        """
        Copy a file
        src: source file path
        dst: destination file path
        """
        try:
            src_path = self._resolve_path(src)
            dst_path = self._resolve_path(dst)
            
            if not src_path.exists():
                raise FileNotFoundError(f"Source file not found: {src_path}")
            
            # Create destination directory if needed
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.copy2(src_path, dst_path)
            
            logger.info(f"Copied {src_path} to {dst_path}")
            return str(dst_path)
            
        except Exception as e:
            logger.error(f"Error copying file from {src} to {dst}: {str(e)}")
            raise
    
    def move_file(self, src, dst):
        """
        Move a file
        src: source file path
        dst: destination file path
        """
        try:
            src_path = self._resolve_path(src)
            dst_path = self._resolve_path(dst)
            
            if not src_path.exists():
                raise FileNotFoundError(f"Source file not found: {src_path}")
            
            # Create destination directory if needed
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.move(str(src_path), str(dst_path))
            
            logger.info(f"Moved {src_path} to {dst_path}")
            return str(dst_path)
            
        except Exception as e:
            logger.error(f"Error moving file from {src} to {dst}: {str(e)}")
            raise
    
    def file_exists(self, path):
        """
        Check if a file exists
        path: file path (relative or absolute)
        Returns: True if exists, False otherwise
        """
        try:
            file_path = self._resolve_path(path)
            return file_path.exists() and file_path.is_file()
        except Exception as e:
            logger.error(f"Error checking if file exists {path}: {str(e)}")
            return False
    
    def get_file_info(self, path):
        """
        Get file information
        path: file path (relative or absolute)
        Returns: dict with file info
        """
        try:
            file_path = self._resolve_path(path)
            
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            
            stat = file_path.stat()
            
            return {
                "path": str(file_path),
                "name": file_path.name,
                "size": stat.st_size,
                "created": stat.st_ctime,
                "modified": stat.st_mtime,
                "is_file": file_path.is_file(),
                "is_dir": file_path.is_dir()
            }
            
        except Exception as e:
            logger.error(f"Error getting file info for {path}: {str(e)}")
            raise


if __name__ == "__main__":
    # Test file controller
    controller = FileController()
    
    print(f"Base directory: {controller.base_dir}")
    
    # Create a test file
    print("\nCreating test file...")
    path = controller.create_file("test.txt", "Hello from Zox AI!")
    print(f"Created: {path}")
    
    # Read the file
    print("\nReading file...")
    content = controller.read_file("test.txt")
    print(f"Content: {content}")
    
    # Get file info
    print("\nFile info:")
    info = controller.get_file_info("test.txt")
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # Delete the file
    print("\nDeleting file...")
    controller.delete_file("test.txt")
    print(f"File exists: {controller.file_exists('test.txt')}")
