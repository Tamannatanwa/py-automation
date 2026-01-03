#!/usr/bin/env python3
"""
Todo CLI Application
====================

A simple command-line todo list manager with data persistence.

Author: Tamanna
"""

import json
import os
from datetime import datetime

# File to store tasks
TODO_FILE = "todos.json"

def load_todos():
    """Load todos from JSON file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """Save todos to JSON file"""
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def add_todo(todos, task):
    """Add a new todo"""
    todo = {
        "id": len(todos) + 1,
        "task": task,
        "completed": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✅ Added: {task}")

def list_todos(todos):
    """List all todos"""
    if not todos:
        print("📭 No tasks yet!")
        return
    
    print("\n" + "="*60)
    print("YOUR TODO LIST")
    print("="*60)
    for todo in todos:
        status = "✅" if todo["completed"] else "⬜"
        print(f"{status} {todo['id']}. {todo['task']}")
        print(f"   Created: {todo['created']}")
    print("="*60 + "\n")

def complete_todo(todos, task_id):
    """Mark a todo as complete"""
    for todo in todos:
        if todo["id"] == task_id:
            todo["completed"] = True
            save_todos(todos)
            print(f"✅ Completed: {todo['task']}")
            return
    print(f"❌ Task #{task_id} not found!")

def delete_todo(todos, task_id):
    """Delete a todo"""
    for i, todo in enumerate(todos):
        if todo["id"] == task_id:
            task = todo["task"]
            todos.pop(i)
            # Renumber remaining tasks
            for j, t in enumerate(todos):
                t["id"] = j + 1
            save_todos(todos)
            print(f"🗑️ Deleted: {task}")
            return
    print(f"❌ Task #{task_id} not found!")

def show_menu():
    """Display menu"""
    print("\n" + "="*60)
    print("TODO CLI APPLICATION")
    print("="*60)
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("="*60)

def main():
    """Main application loop"""
    todos = load_todos()
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_todo(todos, task)
            else:
                print("❌ Task cannot be empty!")
        
        elif choice == "2":
            list_todos(todos)
        
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_todo(todos, task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_todo(todos, task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid option! Please choose 1-5.")

if __name__ == "__main__":
    main()
