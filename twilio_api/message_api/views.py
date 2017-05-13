'''
Github : https://github.com/1akshat

'''

from django.shortcuts import render
from twilio.rest import Client
from twilio_api import settings

def home(request):
	return render(request, 'index.html', {})

def sms(request):
	client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

	message = client.messages.create(to='+919600577805', from_='+19543629059', body='This message is sent through twilio api using django framework by akshat.')

	print(message.sid)

	return render(request, 'thankyou.html')
