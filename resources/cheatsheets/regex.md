# 🔍 Regular Expressions Cheatsheet

## Basic Patterns

```python
import re

# Match patterns
re.match(pattern, string)    # Match at start
re.search(pattern, string)   # Find anywhere
re.findall(pattern, string)  # Find all matches
re.sub(pattern, repl, string) # Replace matches
```

## Special Characters

```
.       # Any character (except newline)
^       # Start of string
$       # End of string
*       # 0 or more repetitions
+       # 1 or more repetitions
?       # 0 or 1 repetition
{n}     # Exactly n repetitions
{n,}    # n or more repetitions
{n,m}   # Between n and m repetitions
[]      # Character set
|       # Or
()      # Group
\       # Escape special character
```

## Character Classes

```
\d     # Digit [0-9]
\D     # Not a digit
\w     # Word character [a-zA-Z0-9_]
\W     # Not a word character
\s     # Whitespace
\S     # Not whitespace
```

## Common Patterns

```python
# Email
r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Phone (US format)
r'\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}'

# URL
r'https?://[\w\-.]+(\.\w+)+(/[\w\-./?%&=]*)?'

# IP Address
r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# Date (YYYY-MM-DD)
r'\d{4}-\d{2}-\d{2}'

# Time (HH:MM)
r'([01]?\d|2[0-3]):[0-5]\d'
```

## Examples

```python
import re

# Find all emails
text = "Contact: john@example.com or jane@example.com"
emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
print(emails)  # ['john@example.com', 'jane@example.com']

# Validate phone number
phone = "(123) 456-7890"
pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
if re.match(pattern, phone):
    print("Valid phone number")

# Replace dates
text = "Date: 2024-01-15"
new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', text)
print(new_text)  # Date: 01/15/2024
```

---

📖 **Practice regex at: regex101.com**
