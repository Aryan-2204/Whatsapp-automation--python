#install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid='YOUR_TWILIO_ACCOUNT_SID'
auth_token='YOUR_TWILIO_AUTH_TOKEN'

client=Client(account_sid, auth_token)

#design a function to send message

def send_message(recipent_number,message_body):
    try:
        message=client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipent_number}'
        )
        print(f"Message sent successfully ! Message SID{message.sid}")
    except Exception as e:
        print("An error occured",e)


#user input for recipient number and message body
name=input(" Enter the recipient name: ")
recipent_number=input(f"Enter the phone number of {name} with country code (e.g +91): ")
message_body=input(f"Enter the messgae you want to send to {name} :")

#date/time
date_str=input("Enter the date to send message (YYYY-MM-DD): ")
time_str=input("Enter the time to send message (HH:MM in 24-hour format): ")
    
#schedule time    
schedule_datetime = datetime.strptime(
    f"{date_str.strip()} {time_str.strip()}",
    "%Y-%m-%d %H:%M"
)
print("DEBUG:", repr(f"{date_str} {time_str}"))
current_datetime=datetime.now()

time_difference=(schedule_datetime - current_datetime)
delay_seconds = time_difference.total_seconds()

if delay_seconds <=0:
    print("Scheduled time is in the past. Please enter a future date and time ")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}")
    time.sleep(delay_seconds) #wait until schedule time
    send_message(recipent_number,message_body)


    