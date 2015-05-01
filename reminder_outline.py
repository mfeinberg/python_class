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
import sqlite3
import sys

# set up database connection
connection = sqlite3.connect #connection to DB
cursor = connection.cursor() #lets us manipulate DB

# write our schema statement, e.g. CREATE TABLE reminders (id INTEGER PRIMARY KEY)
#task_description text, datetime text, expired boolean, location text, notes text
sql_schema = 'CREATE TABLE IF NOT EXISTS reminders(taskid INTEGER PRIMARY KEY, task TEXT, date TEXT, location TEXT, notes TEXT, expired BOOLEAN)'
# note, integer primary key fields are autoincremented by default
# create db table if not already existing
#use the cursor to create the new table
cursor.execute(sql_schema)

def getNewEvent():
  prompt = 'Press [ENTER] to add a task of q/Q to quit '
  response = raw_input(prompt).strip()
  if responese in ['q','Q','quit','Quit','QUIT','EXIT','Exit','exit']:
   sys.exit() #a way of quitting the program
  else:
   task = raw_input('Task: ')
   year = raw_input('Year (yyyy): ')
   month = raw_input('Month (mm): ')
   day = raw_input('Day (dd): ')
   hour = raw_input('Hour (hh): ')
   minute = raw_input('Minute (mm): ')
   am_or_pm = raw_input('AM or PM: ')
   notes = raw_input('Additional information: ')
   
   data = [task,year,month,day,hour,minute,notes]
   
   cursor.execute('INSERT INTO reminders (task)

def commitNewEvent(event):
  pass
  
def getNMostRecent(N=4):
  pass

def getUpcomingEvents(N=4):
  pass

def mainLoop():
  pass

mainLoop()
