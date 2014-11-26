#!/usr/bin/python
import cgi
import datetime
import time
import os
import Cookie
import cgitb # to facilitate debugging
import sqlite3 # database work
import json #for array encoding


#---------Connect to Database-------
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
#-----------------------------------
cookie_string = os.environ.get('HTTP_COOKIE')  # assign string username to cookie
cook = Cookie.SimpleCookie(cookie_string)
username = cook['username'].value

#x = {}
#x["name"] = "Morgan"
#x["age"] = 20 


#-----------Header---------------------
print "Content-type: application/json"
# don't forget the extra newline!
print
#--------------------------------------  
input = cgi.FieldStorage()
output = input.getvalue("param", None) # this data should come from the ajax call in "character_data.py"
#print json.dumps(output.strip())
data = {}
for row in c.execute('select * from characters where name = ?',(output.strip(),)): #Read for existing user account
        if len(row) != 0:
			#print json.dumps("hello")
			data["name"] = row[1]
			data["lvl"] = row[2]
			data["str"] = row[3]
			data["dex"] = row[4]
			data["con"] = row[5]
			data["int"] = row[6]
			data["wis"] = row[7]
			data["chr"] = row[8]
			data["hpc"] = row[9]
			data["hpm"] = row[10]

#output_new = output[1:]
#chars = c.execute('select * from characters where user = ?',(username,))
#for row in chars:
    #print row[1]
    
#print output
print json.dumps(data)
				
