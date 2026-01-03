#!/usr/bin/env python3
"""
Basic Web Scraper
=================

Introduction to web scraping with BeautifulSoup.

Author: Tamanna
"""

# Note: This is a template. Actual scraping depends on website structure.
# Always check robots.txt and terms of service before scraping.

print("="*60)
print("WEB SCRAPING BASICS")
print("="*60)
print()

try:
    from bs4 import BeautifulSoup
    import requests
    
    print("✅ Required libraries imported successfully!")
    print()
    
    # Example structure (commented out to avoid actual requests)
    print("Basic Web Scraping Pattern:")
    print("-"*40)
    print("""
# 1. Send HTTP request
# response = requests.get('https://example.com')

# 2. Parse HTML content
# soup = BeautifulSoup(response.content, 'html.parser')

# 3. Find elements
# titles = soup.find_all('h1')

# 4. Extract data
# for title in titles:
#     print(title.text)

# 5. Process and store data
    """)
    
    print("\n📚 Learn more at: https://www.crummy.com/software/BeautifulSoup/")
    
except ImportError:
    print("❌ Missing required libraries!")
    print("Install with: pip install requests beautifulsoup4")

print()
print("="*60)
