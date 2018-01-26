> Steps to get birthday list from facebook

- Go to your facebook account
- Left hand side you will see "Event" click on that
![Event](https://github.com/Singhak/Python_Stuff/blob/master/readme_res/event.PNG)
- After click a new page will be open.
- Now on scroll down the page
- Right hand side of that page there is a section in which "Upcoming event" and "Birthday" mention
![Bdy](https://github.com/Singhak/Python_Stuff/blob/master/readme_res/bdy.PNG) 
- Right click on "Birthday" and copy link address. Which will be look like this "webcal://www.facebook.com/ical/b.php?uid=1000008781234978&key=AQHBxgzG-4deOJ0h"
- Paste that link without "webcal://" only "www.facebook.com/ical/b.php?uid=1000008781234978&key=AQHBxgzG-4deOJ0h" in browser.
- It will download a file.

> Steps to run bdyreminder.py

- Above downloaded file rename it to "cal.ics"
- Keep that file same place where you will keep "bdyreminder.py"
- Simply run it "python bdyreminder.py"
- If you will not keep "cal.ics" file same place then run like this "python bdyreminder.py <path_of_cal.ics>

> Steps to install icalendar pakage

- Download zip from [icalendar](https://pypi.python.org/pypi/icalendar)
- Unzip the zip file
- Goto inside folder where setup.py exist
- Open Terminal/Cmd at same place
- then run "python setup.py install"

