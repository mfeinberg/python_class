'''
Reminder Application
A bare-bones task management application
TODAY
0. Talk about our schema
1. set up an sqlite3 database 
2. get user's task information 
3. convert the user's date and time information into a datetime object
4. commit our formatted user input to the database
5. get the <N> most recent tasks 
NEXT WEEK:
1. Improve the interface so we have options to ...
2. Provide task modification capabilities
3. modify our program so it takes command line arguments. Args include:
 - Number of weeks out to show tasks for
4. Abstract our database into a module and import that
5. Load schema from a file with executescript method
6. Have the reminder.py script email us with upcoming events
'''

# imports
import datetime
import sys
import sqlite3

# set up database connection
connection = sqlite3.connect('C:\Users\Matthew\Desktop\myDB.db') #connection to DB
cursor = connection.cursor() #lets us manipulate DB

# write our schema statement, e.g. CREATE TABLE reminders (id INTEGER PRIMARY KEY)
# task_description text, date text, expired boolean, location text, notes text
sql_schema = '''CREATE TABLE IF NOT EXISTS reminders(task_id INTEGER PRIMARY KEY,
task TEXT, date TEXT, location TEXT, notes TEXT, expired BOOLEAN)'''
# note, integer primary key fields are autoincremented by default
# use the cursor to create the new table
cursor.execute(sql_schema)

def getEvent(): #collect all fields for an event
	task = raw_input('task: ').strip()
	year = raw_input('year (YYYY): ').strip()
	month = raw_input('month (MM) : ').strip()
	day = raw_input('day (DD): ').strip()
	hour = raw_input('hour (HH): ').strip()
	minute = raw_input('minute (MM): ').strip()
	am_or_pm = raw_input('am or pm: ').strip()
	location = raw_input('location: ').strip()
	notes = raw_input('additional information: ').strip()
	
	#use datetime.datetime to create a timestring object
	time_string = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute))
	expired = time_string < datetime.datetime.now()
	event = (task,time_string,location,notes,expired)
	
	return event
	
def getNewEvent():
	while 1:
		prompt = 'Press [ENTER] to add a task or q/Q to quit: '
		response = raw_input(prompt).strip()
		if response in ['q','Q']:
			break
		else:
			event = getEvent()
			commitNewEvent(event)					
				
def commitNewEvent(event):
	cursor.execute('INSERT INTO reminders (task, date, location, notes, expired) \
	VALUES (?,?,?,?,?)', event)
	# commit this with connection.commit(), then fetch to make sure it worked
	connection.commit()
  
def getMostRecent():
  expired_events = connection.execute('SELECT * FROM reminders WHERE expired = 1')
  for row in expired_events:
	for field in row:
		print field
	print '#####'

def getUpcomingEvents():
  expired_events = connection.execute('SELECT * FROM reminders WHERE expired = 0')
  for row in expired_events:
	for field in row:
		print field
	print '#####'

def alterEvent():
	while 1:
		prompt = "Would you like to edit an event? Y/N: "
		response = raw_input(prompt).strip()
		if response in ['n','N','no','No','NO']:
			break
		else:
			print "Here is a list of your events:"
			events = cursor.execute('SELECT task_id, task FROM reminders')
			for row in events:
				for field in row:
					print field,
				print '\n'
			prompt = "Please enter the number of the task you want to change: "
			response_id = raw_input(prompt).strip()
			print "\nThis is the full event listing:"
			event_to_alter = cursor.execute('SELECT * FROM reminders WHERE task_id = ?', response_id)
			for row in event_to_alter:
				for field in row:
					print field
			print "Please enter the updated information:"
			altered_event = getEvent()
							
			cursor.execute('UPDATE reminders SET task = ?, date = ?, location = ?, notes = ?, expired = ? \
			WHERE task_id = ?', (altered_event[0], altered_event[1], altered_event[2],altered_event[3],altered_event[4], response_id))
			# commit this with connection.commit(), then fetch to make sure it worked
			
			changed_event = cursor.execute('SELECT * FROM reminders WHERE task_id = ?', response_id)
			for row in changed_event:
				for field in row:
					print field
			

def mainLoop():
	getNewEvent()
	#getMostRecent()
	#getUpcomingEvents()
	alterEvent()

mainLoop()

