# My program is a powerful tool that should only be used for authorized ethical hacking actions
# and in compliance with current laws and regulations. I assume no responsibility for the improper
# or illegal use of the program.

import sqlite3, os, datetime

# function line
def Line():
    print('\n', '- - - - - - - - - -\n')

# function Call log analysis
def CallLog():
    Line()

    print('\n Call log \n')

    # Input table name
    tab_n = input('Table name: ')

    # adb call log
    # Execute the adb command and save the output to a file
    command = "adb shell content query --uri content://call_log/calls > call_log.txt"

    os.system(command)

    # Import the data into the SQLite database
    os.system(f"sqlite3 {DB} '.mode csv' '.headers on' '.import call_log.txt {tab_n}'")

    # Delete the temporary file
    os.remove("call_log.txt")

    # DB connection
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Select table values
    cursor.execute(f"SELECT * FROM {tab_n}")

    # Fetch all values
    rows = cursor.fetchall()

    # Print the values in order
    for row in rows:
        print(row, '\n - - - \n')

    # Close the connection
    conn.close()

# Function sms log
def SMSlog():
    Line()

    print('\n SMS log \n')

    # Input table name
    tab_n = input('Table name: ')

    # adb call log
    # Execute the adb command and save the output to a file
    command = "adb shell content query --uri content://sms/ > sms_log.txt"

    os.system(command)

    # Import the data into the SQLite database
    os.system(f"sqlite3 {DB} '.mode csv' '.headers on' '.import sms_log.txt {tab_n}'")

    # Delete the temporary file
    os.remove("sms_log.txt")

    # DB connection
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Select table values
    cursor.execute(f"SELECT * FROM {tab_n}")

    # Fetch all values
    rows = cursor.fetchall()

    # Print the values in order
    for row in rows:
        print(row, '\n - - - \n')

    # Close the connection
    conn.close()

# Function save the sdcard files
def PullAndroidFiles():
    Line()

    print('\n Android files \n')

    F_Destination = input("Destination (tree or Folder name): ")
    print('\n Coping... \n')
    os.system(f"sudo adb pull /sdcard {F_Destination}")
    print("\n Done. \n")

# Print title
os.system('figlet -f slant adbForensic && sleep 1')

# Input database name
DB = input('New DB device name (with .db): ')

# Create DB
os.system(f"touch {DB}")

CallLog()
SMSlog()
PullAndroidFiles()
