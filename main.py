# importing required resources
import codecs
import schedule
import json
import smtplib
from whoisapi import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# required parameters
API_key = "at_0DAwfe5d2oGlyOORVFlo2k65Rmd9N"
client = Client(api_key=API_key)
client.parameters.output_format = 'JSON'
params = RequestParameters(ignore_raw_texts=1)


# function to store and manipulate required data
def query_API(url):
    resp_str = client.data(url)
    created_date = resp_str.created_date
    updated_date = resp_str.updated_date
    expiry = resp_str.expires_date
    schedule.every(24).hours.do(query_API, API_link)
    return created_date, updated_date, expiry


def json_formatting(data1, data2):
    original_query = json.loads(data1, indent=4, sort_keys=True)
    next_query = json.loads(data2, indent=4, sort_keys=True)
    if sorted(a.items()) == sorted(b.items()):
        pass
    else:
        # structuring email
        msg = MIMEMultipart('alternative')
        msg['From'] = 'luis_mb@hotmail.es'
        msg['To'] = 'luisdmb1901@gmail.com'
        msg['Subject'] = f"Recent Changes from {API_link}"
        greeting = "Hello, please find attached the changes found."
        email_part1 = MIMEText(greeting, 'plain')
        msg.attach(email_part1)

        # JSON file creation and formatting
        filename = f"{API_link}_changes.json"
        with open(filename) as data_file:
            data = json.load(data_file)

        file_format = f = codecs.open(filename, "r", "utf-8")
        attachment = MIMEText(file_format.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)

        # Connecting to smtplib and send email changes.
        s = smtplib.SMTP()
        s.connect()
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()


# storage for required link
API_link = "google.com"

js = query_API(API_link)
print(js)
