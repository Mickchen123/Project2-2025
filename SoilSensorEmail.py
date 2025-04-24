import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
import schedule

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

from_email_addr = "REPLACE_WITH_THE_SENDER_EMAIL"
from_email_pass = "REPLACE_WITH_THE_SENDER_EMAIL_APP_PASSWORD"
to_email_addr = "REPLACE_WITH_THE_RECIPIENT_EMAIL"

def callback(channel):
    if GPIO.input(channel):
        plant_status = "Water NOT needed"
    else:
        plant_status = "Please water your plant"
    msg = EmailMessage()
    body = plant_status
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Plant Status Update'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.sendmail(from_email_addr, to_email_addr, msg.as_string())
    server.quit()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

def check_plant_status():
    callback(channel)

schedule.every().day.at("08:00").do(check_plant_status)
schedule.every().day.at("12:00").do(check_plant_status)
schedule.every().day.at("16:00").do(check_plant_status)
schedule.every().day.at("20:00").do(check_plant_status)

while True:
    schedule.run_pending()
    time.sleep(1)
