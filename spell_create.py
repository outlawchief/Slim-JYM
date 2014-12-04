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
    spellname = form.getvalue("spellname", None)
    classname = form.getvalue("classname", None)
    dicecount = form.getvalue("dicecount", None)
    dice = form.getvalue("dice", None)
    details = form.getvalue("details", None)
    print spellname

    if spellname != None:
        try:
            c.execute('insert into spells values(?,?,?,?,?);', (spellname, classname, dicecount, dice, details))
            conn.commit()
        except sqlite3.OperationalError:
            c.execute('CREATE TABLE spells(spellname varchar(100), classname varchar(100), dicecount int, dice int, details varchar(500))')
            conn.commit()
            c.execute('insert into spells values(?,?,?,?,?);', (spellname, classname, dicecount, dice, details))
            conn.commit()

    #print"<h1>Congratulations!</h1>"
     #except sqlite3.OperationalError:



print'''

<form method = 'post' action = 'spell_create.py' id='info'>
Spell name: <input type='text' name='spellname'>
</br>
Classes and Spell level: <input type='text' name='classname'>
</br>
Number of Dice: <input type='text' name='dicecount'>
</br>
Sides per dice: <input type='text' name='dice'>
</br>

Any details on the spell(damage type, area of affect, save, etc): <input type='text' name='details'>
</br>

'''
print "<input type = 'submit'>"
print "</form>"
print "<br>"
print "<form method = 'post' action = 'account_page1.py'>"
print "<input type = 'submit' value = 'User Page' >"
print "</form>"


print "</body>"
print "</html>"
