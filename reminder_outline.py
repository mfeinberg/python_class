Skip to content
 This repository
Explore
Gist
Blog
Help
@mfeinberg mfeinberg
 
 Watch 1
  Star 1
  Fork 1
pythonwithalex/Spring2015
 branch: master  Spring2015/week4/reminder/reminder_outline.py
@pythonwithalexpythonwithalex 3 hours ago Update reminder_outline.py
1 contributor
RawBlameHistory     56 lines (37 sloc)  1.163 kb
#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

# set up database connection

# write our schema statement, e.g. CREATE TABLE reminders (id INTEGER PRIMARY KEY)
# note, integer primary key fields are autoincremented by default

# create db table if not already existing

def getNewEvent():
  pass

def commitNewEvent(event):
  pass
  
def getNMostRecent(N=4):
  pass

def getUpcomingEvents(N=4):
  pass

def mainLoop():
  pass

mainLoop()
Status API Training Shop Blog About
© 2015 GitHub, Inc. Terms Privacy Security Contact
