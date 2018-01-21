import sys, requests
from datetime import datetime
import json
#from urllib2 import urlopen
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if data.get('ip'):
	ip = data['ip']
else:
	ip = 'No ip'
	
if data.get('postal'):
	postal = data['postal']
else:
	postal = 'No postal'

if data.get('city'):
	city = data['city']
else:
	city = 'No city'
	
if data.get('loc'):
	loc = data['loc']
else:
	loc = 'No loc'
	
if data.get('country'):
	country = data['country']
else:
	country = 'No country'

if data.get('region'):
	region = data['region']
else:
	region = 'No region'


# print 'Your IP detail\n '
body =  'IP : {0} \nRegion : {1} \nCountry : {2} \nCity : {3} \nPincode : {4} \nlat-log: {5} \ntime: {6}'.format(ip,region,country,city,postal,loc, time)
print body

def send_email(recipient, subject, body):
	import smtplib
	FROM = <sender_email_id>
	gmail_pwd = <pwd_of_sender_eamilid>'
	TO = recipient if type(recipient) is list else [recipient]
	SUBJECT = subject
	TEXT = body

	# Prepare actual message
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.ehlo()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		server.close()
		print ('successfully sent the mail')
	except Exception as e:
		with open("H:/Pythoon_stuffs/log.txt", "a") as myfile:
			myfile.write(str(e))
		print ("failed to send mail " +str(e))
		
send_email('anilsingh.singh09@gmail.com', 'Somebody Login', body)