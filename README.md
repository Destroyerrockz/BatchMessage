# BatchMessage
Sends a sms and email to multiple people contacts fetched from a sqlite database.


## Requirements: -

Python (Only tested on 3.6) 

Python modules:-
- Twilio: pip install twilio.
- PyQt5: pip install pyqt5.
- PyQt5 Tools: pip install pyqt5-tools.

You need to have a:-

- sqlite database which contains the contacts i.e email id and phone numbers
- twilio account and your twilio ACCOUNT SID, AUTH TOKEN and Twilio Number
- email account, email id, password and a SSL supported mail server of your email provider. For eg:- smtp.gmail.com

## Steps:-

1. Clone the repo.

2. Run mainw.py. Go to File> Settings.

3. Select your database file and enter the data corresponding to the label in each tab SQLite, Twilio, Email. (I think they are rather self explanatory, I may be wrong)

4. Click on OK.

5. Go to main window of the program fill the subject and message and click on Send SMS button to send SMS on Send Email to send Email and on Send Both to send Both.

6. The Program may freeze as I am yet to implement multi-threading so don't panic. You will get a success messagebox when it's done.
