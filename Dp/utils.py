
from twilio.rest import Client
from django.conf import settings

# Your Twilio account SID and auth token
account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN

# Create a Twilio client object
client = Client(account_sid, auth_token)

def send_sms(to_number, message):
    # The phone number to send the SMS message from (must be a Twilio phone number)
    from_number = settings.TWILIO_PHONE_NUMBER

    # Send the SMS message using the Twilio client
    message = client.messages.create(to=to_number, from_=from_number, body=message)
    return message