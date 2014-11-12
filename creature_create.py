#!/usr/bin/python
import cgi
import datetime
import time
import os
import Cookie
import cgitb # to facilitate debugging
import sqlite3 # database work

#---------Connect to Database-------
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
#-----------------------------------
cookie_string = os.environ.get('HTTP_COOKIE')  # assign string username to cookie
cook = Cookie.SimpleCookie(cookie_string)
username = cook['username'].value

#-----------Header---------------------
print "Content-type: text/html"
# don't forget the extra newline!
print
#--------------------------------------
print "<html>"
print "<body>"

form = cgi.FieldStorage() #variable "form" becomes a buffer array from passed in data

if form != None:
    charactername = form.getvalue("charname", None) #get variable "username" from buffer
    level = form.getvalue("level", None) #get variable "password" from buffer
    strength = form.getvalue("charstr", None) #Do we remember the session post session
    dexterity = form.getvalue("chardex", None)
    constitution = form.getvalue("charcon", None)
    intelligence = form.getvalue("charint", None)
    wisdom = form.getvalue("charwis", None)
    charisma = form.getvalue("charcha", None)
    HP = form.getvalue("charhp", None)
    print charactername
    print level
    print dexterity
    print constitution
    print intelligence
    print wisdom
    print HP
    
    if charactername != None:
        c.execute('insert into characters values(?,?,?,?,?,?,?,?,?,?,?);', (username,charactername, level,strength,dexterity,constitution,intelligence,wisdom,charisma,HP,HP))
        conn.commit()
    #print"<h1>Congratulations!</h1>"
     #except sqlite3.OperationalError:
         


print'''

<form method = 'post' action = 'creature_create.py' id='info'>
Character name: <input type='text' name='charname'>
</br>
Level: <input type='text' name='level'>
</br>
Strength: <input type='text' name='charstr'>
</br>
Dexterity: <input type='text' name='chardex'>
</br>

Constitution: <input type='text' name='charcon'>
</br>

Intelligence: <input type='text' name='charint'>
</br>

Wisdom: <input type='text' name='charwis'>
</br>

Charisma: <input type='text' name='charcha'>
</br>

HP: <input type='text' name='charhp'>
'''
print "<input type = 'submit'>"
print "</form>"


print "</body>"
print "</html>"
