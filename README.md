# SysAlertMonitor

## Automated System Monitoring and Notification

## Overview
This project provides an automated solution for monitoring system resources including CPU, memory, and disk usage on a machine. Utilizing Python, the script uses the `psutil` library for real-time metric collection and `smtplib` for sending email alerts when thresholds are exceeded. It's an ideal tool for system administrators who need to be promptly notified about potential system overloads.

## Features
- **Real-Time Monitoring**: Automatically collects metrics on CPU, memory, and disk usage.
- **Configurable Thresholds**: Set custom thresholds for when alerts should be triggered.
- **Email Alerts**: Sends automatic notifications via email when thresholds are exceeded.
- **Logging**: Keeps a log of system metrics for record-keeping and analysis.

## Prerequisites
Before you run this script, ensure you have:
- `psutil` library installed (`pip install psutil`).
- SMTP server credentials for sending email alerts.
- Additionally, you have to setup app passwords on your google account to acccess it in the script
