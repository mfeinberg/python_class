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
connection = sqlite3.connect('db.db') #connection to DB
cursor = connection.cursor() #lets us manipulate DB

# write our schema statement, e.g. CREATE TABLE reminders (id INTEGER PRIMARY KEY)
# task_description text, date text, expired boolean, location text, notes text
sql_schema = '''CREATE TABLE IF NOT EXISTS reminders(task_id INTEGER PRIMARY KEY,
task TEXT, date TEXT, location TEXT, notes TEXT, expired BOOLEAN)'''
# note, integer primary key fields are autoincremented by default
# use the cursor to create the new table
cursor.execute(sql_schema)


def getNewEvent():
	prompt = 'Press [ENTER] to add a task or q/Q to quit'
	response = raw_input(prompt).strip()
	if response in ['q','Q']:
		sys.exit()

	else:
	#might have to go back to original code
		data = [] #empty list that will be filled w/ user info and then inserted into DB
		user_info = ['task: ','year (YYYY): ','month (MM) : ','day (DD): ','minute (MM): ','am or pm: ','location: ','additional information: ']
		for question in user_info:
			data.append(raw_input(question).strip())
		time_date = [int(item) for item in data[1:5]]
		time_string = datetime.datetime(time_data)
		#task = raw_input('task: ').strip()
		#year = raw_input('year (YYYY): ').strip()
		#month = raw_input('month (MM) : ').strip()
		#day = raw_input('day (DD): ').strip()
		#hour = raw_input('hour (HH): ').strip()
		#minute = raw_input('minute (MM): ').strip()
		#am_or_pm = raw_input('am or pm: ').strip()
		#location = raw_input('location: ').strip()
		#notes = raw_input('additional information: ').strip()
		expired = time_string < datetime.datetime.now()
				
		# use datetime.datetime to create a timestring object
		#time_string = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute))
		
		#data = (task,time_string,location,notes,expired)
		cursor.execute('INSERT INTO reminders (task, date, location, notes, expired) \
		VALUES (?,?,?,?,?)', data)
		# commit this with connection.commit(), then fetch to make sure it worked
		connection.commit()
		
		rows = cursor.execute('SELECT * FROM reminders')
		#row == record
		for row in rows:
			for field in row:
				print field
			print '####' #breaks up records/neatly separates the different records

def commitNewEvent(event):
  pass
  
def getNMostRecent(N=4):
  pass

def getUpcomingEvents(N=4):
  pass


def mainLoop():
  getNewEvent()

mainLoop()
