#!/usr/bin/env python3
"""
Send Email with Python
======================

Basic email sending example.

Author: Tamanna
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Send an email using SMTP.
    
    Args:
        sender_email: Your email address
        sender_password: Your email password (use app password for Gmail)
        recipient_email: Recipient's email address
        subject: Email subject
        body: Email body text
    """
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Connect to SMTP server (Gmail example)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Enable security
        
        # Login
        server.login(sender_email, sender_password)
        
        # Send email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        
        print("✅ Email sent successfully!")
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        
    finally:
        server.quit()

if __name__ == "__main__":
    print("="*60)
    print("EMAIL AUTOMATION EXAMPLE")
    print("="*60)
    print()
    print("Template for sending emails with Python")
    print()
    print("⚠️  Security Tips:")
    print("- Use environment variables for credentials")
    print("- Never commit passwords to version control")
    print("- Use app-specific passwords for Gmail")
    print()
    print("Example usage:")
    print('''
# Set up environment variables
import os
sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
recipient = "recipient@example.com"

send_email(sender, password, recipient, "Test", "Hello!")
    ''')
    print()
    print("="*60)
