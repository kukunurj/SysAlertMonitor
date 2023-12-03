# Author: Jai Reddy Kukunuru
# Program to monitor system usage and send alert notification 

import psutil  
import smtplib 

# library to create email messages
from email.mime.text import MIMEText #text content
from email.mime.multipart import MIMEMultipart #text and attachments

import logging
from datetime import datetime

# logging set up
logging.basicConfig(filename='system_monitor.log', level=logging.INFO)

def send_email(subject, body):
    # Your email configuration
    # change sender, receiver, password of sender accordingly. 

    sender_email = "xyz@abc.com"
    receiver_email = "xyz@abc.com"
    password = "xyzabc"

    # Email setup
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls() # connection secure using TLS
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string()) 

def monitor_system():
    # Monitoring thresholds (customize based on your needs)
    cpu_threshold = 70
    memory_threshold = 80
    disk_threshold = 70

    # Get system metrics
    cpu_usage = psutil.cpu_percent(interval=1) # cpu usage over 1 second
    memory_usage = psutil.virtual_memory().percent 
    disk_usage = psutil.disk_usage('/').percent 

    # Log metrics
    logging.info(f"{datetime.now()} - CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Disk Usage: {disk_usage}%")

    # Check thresholds and send alerts if exceeded
    if cpu_usage > cpu_threshold:
        send_email("High CPU Usage Alert", f"Current CPU Usage: {cpu_usage}%")

    if memory_usage > memory_threshold:
        send_email("High Memory Usage Alert", f"Current Memory Usage: {memory_usage}%")

    if disk_usage > disk_threshold:
        send_email("High Disk Usage Alert", f"Current Disk Usage: {disk_usage}%")

if __name__ == "__main__":
    # Run system monitoring
    monitor_system()

