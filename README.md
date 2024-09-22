<strong> <h1> adbForensic: A Powerful Tool for Android Forensic Analysis </h1> </strong> <br>

<strong> <h2> Warning </h2> </strong> <br>

<h3>
  This program is a powerful tool that should only be used for authorized ethical hacking actions and in compliance with current laws and regulations. <br>
  I assume no responsibility for the improper or illegal use of the program. <br>
</h3>

<h2> Overview </h2> <br>

<h3>
  adbForensic is a Python script designed to facilitate Android forensic analysis. <br>
  It provides a set of functions to extract and analyze data from an Android device, including call logs, SMS logs, and files from the SD card. <br>
</h3>

<h2> Features </h2> <br>

<h2> Call Log Analysis </h2> <br>

<h3>
  The CallLog function extracts the call log from the Android device using the adb command and imports the data into a SQLite database. <br>
  The function then prints the call log data in a readable format. <br>
</h3>

<h2> SMS Log Analysis </h2> <br>

<h3>
  The SMSlog function extracts the SMS log from the Android device using the adb command and imports the data into a SQLite database. <br>
  The function then prints the SMS log data in a readable format. <br>
</h3>

<h2> SD Card File Extraction </h2> <br>

<h3>
  The PullAndroidFiles function pulls files from the SD card of the Android device using the adb command and saves them to a specified destination folder. <br>
</h3>

<h2> Usage </h2> <br>

<h3>
  Run the script and enter the desired database name (with .db extension) when prompted. <br>
  The script will create the database and execute the CallLog, SMSlog, and PullAndroidFiles functions. <br>
  Follow the prompts to input the table name for the call log and SMS log analysis, and the destination folder for the SD card file extraction. <br>
</h3>

<h2> Requirements </h2> <br>

<h3> Python 3.x </h3> <br>
<h3> adb command-line tool </h3> <br>
<h3> sqlite3 command-line tool </h3> <br>
<h3> figlet command-line tool (optional, for generating the script title) </h3> <br>
