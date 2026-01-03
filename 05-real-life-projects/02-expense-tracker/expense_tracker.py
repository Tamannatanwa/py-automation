#!/usr/bin/env python3
"""
Expense Tracker
===============

Track and analyze your expenses.

Author: Tamanna
"""

import csv
import os
from datetime import datetime

EXPENSE_FILE = "expenses.csv"

def initialize_file():
    """Create CSV file if it doesn't exist"""
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense(category, description, amount):
    """Add a new expense"""
    date = datetime.now().strftime("%Y-%m-%d")
    with open(EXPENSE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, amount])
    print(f"✅ Added expense: {description} - ${amount}")

def view_expenses():
    """View all expenses"""
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet!")
        return
    
    print("\n" + "="*70)
    print("ALL EXPENSES")
    print("="*70)
    
    total = 0
    with open(EXPENSE_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['Date']} | {row['Category']:15} | {row['Description']:20} | ${row['Amount']:>8}")
            total += float(row['Amount'])
    
    print("="*70)
    print(f"TOTAL: ${total:.2f}")
    print("="*70 + "\n")

def category_report():
    """Show expenses by category"""
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet!")
        return
    
    categories = {}
    with open(EXPENSE_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row['Category']
            amount = float(row['Amount'])
            categories[cat] = categories.get(cat, 0) + amount
    
    print("\n" + "="*50)
    print("EXPENSES BY CATEGORY")
    print("="*50)
    for cat, amount in sorted(categories.items()):
        print(f"{cat:20} ${amount:>10.2f}")
    print("="*50 + "\n")

def main():
    """Main application"""
    initialize_file()
    
    while True:
        print("\n" + "="*50)
        print("EXPENSE TRACKER")
        print("="*50)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Report")
        print("4. Exit")
        print("="*50)
        
        choice = input("\nChoose (1-4): ").strip()
        
        if choice == "1":
            category = input("Category (Food/Transport/Shopping/etc): ")
            description = input("Description: ")
            try:
                amount = float(input("Amount: $"))
                add_expense(category, description, amount)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            category_report()
        
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid option!")

if __name__ == "__main__":
    main()
