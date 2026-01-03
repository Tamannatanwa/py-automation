#!/usr/bin/env python3
"""
Organize Files by Extension
============================

Automatically organize files into folders based on their extensions.

Author: Tamanna
"""

import os
import shutil
from pathlib import Path

def organize_files(directory):
    """
    Organize files in a directory by their extensions.
    
    Args:
        directory: Path to the directory to organize
    """
    # Define file categories
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt'],
        'Spreadsheets': ['.xlsx', '.xls', '.csv'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.java', '.cpp', '.html', '.css']
    }
    
    directory = Path(directory)
    
    # Count files organized
    organized_count = 0
    
    # Iterate through files
    for file_path in directory.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()
            
            # Find category for file
            moved = False
            for category, extensions in categories.items():
                if extension in extensions:
                    # Create category folder if it doesn't exist
                    category_path = directory / category
                    category_path.mkdir(exist_ok=True)
                    
                    # Move file to category folder
                    destination = category_path / file_path.name
                    shutil.move(str(file_path), str(destination))
                    print(f"Moved: {file_path.name} → {category}/")
                    organized_count += 1
                    moved = True
                    break
            
            # Handle uncategorized files
            if not moved and extension:
                other_path = directory / "Other"
                other_path.mkdir(exist_ok=True)
                destination = other_path / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"Moved: {file_path.name} → Other/")
                organized_count += 1
    
    print(f"\n✅ Organized {organized_count} files!")

if __name__ == "__main__":
    # Example usage (create test directory)
    test_dir = "/tmp/organize_demo"
    os.makedirs(test_dir, exist_ok=True)
    
    # Create some test files
    test_files = ["document.pdf", "image.jpg", "video.mp4", "script.py"]
    for file in test_files:
        Path(f"{test_dir}/{file}").touch()
    
    print("Organizing files...")
    organize_files(test_dir)
    print(f"\nCheck {test_dir} to see organized files!")
