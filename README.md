# SysAlertMonitor

## Automated System Monitoring and Notification

## Overview
This project provides an automated solution for monitoring system resources such as CPU, memory, and disk usage. It utilizes Python for scripting, leverages `psutil` for real-time metric collection, uses `smtplib` for email alerts, and employs logging for record-keeping. The project is ideal for system administrators needing timely notifications about their systems' status.

## Key Features
**Real-Time Monitoring**: Automatically collects metrics on CPU, memory, and disk usage.
**Configurable Thresholds**: Set custom thresholds for alert triggering.
**Email Alerts**: Sends automatic notifications via email when thresholds are exceeded.
**Logging**: Keeps a log of system metrics for record-keeping and analysis.

## Tools and Technologies
**Python**: Primary language for scripting and automation.
**psutil Library**: Gathers system metrics like CPU, memory, and disk usage.
**smtplib Library**: Facilitates the sending of email notifications.
**Logging Module**: Provides logging capabilities for recording system metrics and events.
**Email.mime Module**: Used for composing emails in MIME format.
**SMTP Server**: An external server (like Gmail or Outlook) for email delivery.
**GitHub**: For version control and collaboration (if the project is hosted on GitHub).

## Prerequisites
`psutil` library (`pip install psutil`)
SMTP server credentials for email alerts


## Configuration
Configure thresholds for CPU, memory, and disk usage in the script.
Set up SMTP server details and recipient email for notifications.
Set up app passwords in google account to send emails using the script.


## References
https://www.geeksforgeeks.org/logging-in-python/
https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta
https://www.geeksforgeeks.org/psutil-module-in-python/
https://www.tutorialspoint.com/python/python_sending_email.htm


