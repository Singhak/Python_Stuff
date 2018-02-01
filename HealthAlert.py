from plyer import notification 
import time
import random
import winsound
#uncomment to use text to speech feature
#import pyttsx 
''' To use pyttsx module you have install this module as well as 'pypiwin32' module also it is working fine in python27 for version 3 you have to change in few file of pyttsx
error to import engine in __init__.py change to from . import engine in some other file import driver change it from . import driver'''

tip = ['Drink Water', 'Blink your eyes', 'Check your posture', 'See 20m away']

#winsound.Beep(500,1500) #frequency, duration
#print (start_time)
def showTip(msg):
	notification.notify(
		title='Health Alert',
		message= msg,
		app_name='Health Tip',
		timeout = 15,
	)

#uncomment line 22-28 to use text to speech feature
#engine = pyttsx.init()
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate-50)
#def speakTip(msg):
#	engine.say(msg)
#	engine.runAndWait()

############################################ with sleep()
#time.sleep(600)	
while(1):
	# winsound.Beep(500,1500) # we can use these also  print('\007') or  print('\a') for beep sound
	winsound.PlaySound('rain2.wav', winsound.SND_FILENAME)
	msg = tip[random.randint(0,3)]
	showTip(msg)
	#uncomment to use text to speech feature
	#speakTip(msg)
	time.sleep(600)

########################################### without sleep()

# start_time = time.time()/(60)
# while(1):
	# curr_time = time.time()/(60)
	# diff = curr_time - start_time
	# # print(diff)
	# if diff >=10 :
		# start_time = curr_time
		# winsound.Beep(500,1500) # we can use these also  print('\007') or  print('\a') for beep sound
		# msg = tip[random.randint(0,3)]
		# showTip(msg)
		# speakTip(msg)