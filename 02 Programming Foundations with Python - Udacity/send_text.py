from twilio.rest import TwilioRestClient

#Your account sid and auth token from twilio.com/user.account
account_sid =
auth_token =
client =TwilioRestClient(account_sid, auth_token)

message = client.sms