from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

call = client.calls.create(
    twiml='<Response><Say>Emergency Fall Detected please respond Thank you</Say></Response>',
    to='+919860215374',
    from_=''
)

print(call.sid)