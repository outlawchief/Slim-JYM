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
#input = cgi.FieldStorage()
name = "jim"
stat = 2
amount = 10
#name = input.getvalue("name", None) # this data should come from the ajax call in "character_data.py"
#stat = input.getvalue("stat", None)
#amount = input.getvalue("amount", None)
if stat == 2:
        c.execute('update characters set lvl = ? where name = ?;',(amount, name))
if stat == 3:
        c.execute('update characters set str = ? where name = ?;',(amount, name))
if stat == 4:
        c.execute('update characters set dex = ? where name = ?;',(amount, name))
if stat == 5:
        c.execute('update characters set con = ? where name = ?;',(amount, name))
if stat == 6:
        c.execute('update characters set intel = ? where name = ?;',(amount, name))
if stat == 7:
        c.execute('update characters set wis = ? where name = ?;',(amount, name))
if stat == 8:
        c.execute('update characters set cha = ? where name = ?;',(amount, name))
if stat == 9:
        c.execute('update characters set hp = ? where name = ?;',(amount, name))

}
conn.commit();
 #Read for existing user account

#output_new = output[1:]
#chars = c.execute('select * from characters where user = ?',(username,))
#for row in chars:
    #print row[1]

#print output
