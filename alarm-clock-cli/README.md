Alarm Clock CLI
Overview

This is a simple Alarm Clock Command Line Interface (CLI) application built using Python.

The application allows users to:

Add an alarm
View alarms
Delete alarms
Start the alarm scheduler
Receive a notification when an alarm is triggered
AI-Assisted Planning

Before coding, AI was used to:

Refine the requirements
Plan the project structure
Identify edge cases
Decide on a simple and clean implementation
Features
Multiple alarms
Time validation (HH:MM:SS)
Prevents past-time alarms
Alarm notification with terminal bell
Simple menu-driven interface
Project Structure
alarm-clock-cli/
├── main.py
├── alarm.py
├── utils.py
├── README.md
└── .gitignore
How to Run

Run the application using:

python main.py
Assumptions
Alarm time must be entered in HH:MM:SS format.
Alarm time should be later than the current system time.
Alarm data is stored in memory and is not saved after the program exits.
Future Improvements
Snooze functionality
Recurring alarms
Save alarms to a file
Unit tests
Better sound notifications
Technologies Used
Python 3
datetime
time
dataclasses
