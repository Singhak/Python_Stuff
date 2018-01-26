import time
import os
import winsound
import sys
from plyer import notification
from collections import namedtuple
from icalendar import Calendar

DEFAULT_CAL = 'cal.ics'

Bday = namedtuple('Bday', 'name bday')


def get_birthdays(cal):
	with open(cal, 'rb') as g:
		gcal = Calendar.from_ical(g.read())
		for component in gcal.walk():
			if component.name == "VEVENT":
				name = component.get('SUMMARY')
				if not name:
					continue
				name = name.replace("'s birthday", "")
				bday = component.get('DTSTART').dt
				bday = bday.strftime('%m%d')
				yield Bday(name=name, bday=bday)


def showMsg(msg):
	notification.notify(
		title='Birthday Reminder',
		message= msg,
		timeout = 15,
	)
 
def checkTodaysBirthdays():
	today = time.strftime('%m%d')
	flag = 0
	for bd in get_birthdays("cal.ics"):
		if today in bd.bday:
			flag =1
			winsound.Beep(500,1500) # we can use these also  print('\007') or  print('\a') for beep sound
			showMsg("Today: " + bd.name +"'s Birthday")
	if flag == 0:
		winsound.Beep(500,1500)
		showMsg("No Birthdays Today!")
 
if __name__ == '__main__':
	if len(sys.argv) < 2:
		cal = DEFAULT_CAL
	else:
		cal = sys.argv[1]
	checkTodaysBirthdays()