<strong> <h1> adbForensic: A Powerful Tool for Android Forensic Analysis </h1> </strong> <br>
<strong> <h2> Warning </h2> </strong>

This program is a powerful tool that should only be used for authorized ethical hacking actions and in compliance with current laws and regulations. I assume no responsibility for the improper or illegal use of the program.
Overview

adbForensic is a Python script designed to facilitate Android forensic analysis. It provides a set of functions to extract and analyze data from an Android device, including call logs, SMS logs, and files from the SD card.
Features
Call Log Analysis

The CallLog function extracts the call log from the Android device using the adb command and imports the data into a SQLite database. The function then prints the call log data in a readable format.
SMS Log Analysis

The SMSlog function extracts the SMS log from the Android device using the adb command and imports the data into a SQLite database. The function then prints the SMS log data in a readable format.
SD Card File Extraction

The PullAndroidFiles function pulls files from the SD card of the Android device using the adb command and saves them to a specified destination folder.
Usage

Run the script and enter the desired database name (with .db extension) when prompted.
The script will create the database and execute the CallLog, SMSlog, and PullAndroidFiles functions.
Follow the prompts to input the table name for the call log and SMS log analysis, and the destination folder for the SD card file extraction.

Requirements

Python 3.x
adb command-line tool
sqlite3 command-line tool
figlet command-line tool (optional, for generating the script title)
