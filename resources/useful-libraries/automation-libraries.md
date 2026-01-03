# 🔧 Useful Python Libraries for Automation

## File and System Automation

### os & pathlib
**Purpose**: File system operations

```python
import os
from pathlib import Path

# os module
os.getcwd()  # Current directory
os.listdir('path')  # List files
os.remove('file.txt')  # Delete file

# pathlib (modern approach)
p = Path('folder/file.txt')
p.exists()  # Check existence
p.mkdir(parents=True)  # Create directory
```

### shutil
**Purpose**: High-level file operations

```python
import shutil

shutil.copy('src.txt', 'dst.txt')  # Copy file
shutil.move('src.txt', 'dst.txt')  # Move file
shutil.rmtree('folder')  # Remove directory tree
```

## Web Automation

### requests
**Purpose**: HTTP requests

```python
import requests

response = requests.get('https://api.example.com')
data = response.json()
```

**Installation**: `pip install requests`

### BeautifulSoup4
**Purpose**: Web scraping

```python
from bs4 import BeautifulSoup
import requests

response = requests.get('https://example.com')
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('h1')
```

**Installation**: `pip install beautifulsoup4 lxml`

### Selenium
**Purpose**: Browser automation

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://example.com')
element = driver.find_element_by_id('username')
element.send_keys('myusername')
```

**Installation**: `pip install selenium`

## Data Processing

### pandas
**Purpose**: Data analysis and manipulation

```python
import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

# Basic operations
df.head()  # First 5 rows
df.describe()  # Statistics
df.groupby('column').mean()  # Grouping
```

**Installation**: `pip install pandas`

### openpyxl
**Purpose**: Excel file operations

```python
from openpyxl import load_workbook

wb = load_workbook('file.xlsx')
ws = wb.active
ws['A1'] = 'Hello'
wb.save('file.xlsx')
```

**Installation**: `pip install openpyxl`

## Email Automation

### smtplib (built-in)
**Purpose**: Sending emails

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Email body')
msg['Subject'] = 'Test'
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('user', 'password')
server.send_message(msg)
server.quit()
```

## Task Scheduling

### schedule
**Purpose**: Simple task scheduling

```python
import schedule
import time

def job():
    print("Running scheduled task")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

**Installation**: `pip install schedule`

## CLI Applications

### click
**Purpose**: Create command-line interfaces

```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('--name', prompt='Your name', help='Your name')
def hello(count, name):
    for _ in range(count):
        click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    hello()
```

**Installation**: `pip install click`

### colorama
**Purpose**: Colored terminal output

```python
from colorama import Fore, Back, Style

print(Fore.RED + 'Red text')
print(Back.GREEN + 'Green background')
print(Style.BRIGHT + 'Bright text')
print(Style.RESET_ALL + 'Normal text')
```

**Installation**: `pip install colorama`

## System Information

### psutil
**Purpose**: System and process utilities

```python
import psutil

# CPU
print(f"CPU Usage: {psutil.cpu_percent()}%")

# Memory
mem = psutil.virtual_memory()
print(f"Memory Usage: {mem.percent}%")

# Disk
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")
```

**Installation**: `pip install psutil`

## Quick Installation

Install all common automation libraries:

```bash
pip install requests beautifulsoup4 selenium pandas openpyxl PyPDF2 schedule click colorama psutil aiohttp python-dotenv
```

---

🚀 **Start automating with these powerful libraries!**
