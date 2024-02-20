
from datetime import datetime, timedelta
import os

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

receiver_email = 'elliotanderson506@gmail.com'
deadlines = [
    {"duedate": "30th Nov, 2021",
    "company": "Apple"
    },
    {"duedate": "19th Dec, 2021",
    "company": "Microsoft"
    },
    {"duedate": "21st Dec, 2021",
    "company": "Amazon"
    },
    {"duedate": "25th Nov, 2021",
    "company": "Reddit"
    },
    {"duedate": "24th Nov, 2021",
    "company": "Amazon"
    }
]

def s_email(company, event_date):

    sender_email = "wolftrackproject@gmail.com"
    # App Password of Gmail Account
    password = "dlafyfekdkmdfjdi"

    subject = "WolfTrack Reminder"

    body = "Dear User," + "\n"\
    "This is a reminder for you to apply for " + str(company) +\
    " as its due date is " + str(event_date) + "\n\n\n" +\
    "Regards \n" +\
    "The WolfTrack Team!"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,text)

    return True

import dateutil.parser
for i in deadlines:
    deadline = dateutil.parser.parse(i['duedate'])
    #alert one day before the deadline
    alertdate = deadline - timedelta(days=1)
    if(alertdate.date()==datetime.now().date()):
        s_email(i['company'], i['duedate'])