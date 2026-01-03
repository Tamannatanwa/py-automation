#!/usr/bin/env python3
"""
Bulk File Renamer
=================

Rename multiple files at once with various patterns.

Author: Tamanna
"""

import os
from pathlib import Path

def bulk_rename(directory, old_pattern, new_pattern):
    """
    Rename files matching a pattern.
    
    Args:
        directory: Path to directory
        old_pattern: Pattern to match in filename
        new_pattern: Replacement pattern
    """
    directory = Path(directory)
    renamed_count = 0
    
    for file_path in directory.iterdir():
        if file_path.is_file() and old_pattern in file_path.name:
            new_name = file_path.name.replace(old_pattern, new_pattern)
            new_path = file_path.parent / new_name
            file_path.rename(new_path)
            print(f"Renamed: {file_path.name} → {new_name}")
            renamed_count += 1
    
    print(f"\n✅ Renamed {renamed_count} files!")

def add_prefix(directory, prefix):
    """Add prefix to all files in directory"""
    directory = Path(directory)
    
    for file_path in directory.iterdir():
        if file_path.is_file():
            new_name = prefix + file_path.name
            new_path = file_path.parent / new_name
            file_path.rename(new_path)
            print(f"Renamed: {file_path.name} → {new_name}")

def number_files(directory, base_name):
    """Rename files with sequential numbering"""
    directory = Path(directory)
    files = [f for f in directory.iterdir() if f.is_file()]
    
    for index, file_path in enumerate(files, 1):
        extension = file_path.suffix
        new_name = f"{base_name}_{index:03d}{extension}"
        new_path = file_path.parent / new_name
        file_path.rename(new_path)
        print(f"Renamed: {file_path.name} → {new_name}")

if __name__ == "__main__":
    print("Bulk File Renamer Demo")
    print("="*50)
    print("\nExample functions available:")
    print("1. bulk_rename(dir, old, new) - Replace pattern")
    print("2. add_prefix(dir, prefix) - Add prefix to files")
    print("3. number_files(dir, base) - Number files sequentially")
    print("\nUse these functions to rename files in your directories!")
