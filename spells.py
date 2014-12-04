#!/usr/bin/python
import cgi
import datetime
import time
import os
import Cookie
import cgitb # to facilitate debugging
import sqlite3 # database work

cgitb.enable()

#database connection to accounts.db
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


cookie_string = os.environ.get('HTTP_COOKIE')
cook = Cookie.SimpleCookie(cookie_string)
username = cook['username'].value

chars = 0
try:
    chars = c.execute('select * from spells;')
except sqlite3.OperationalError: #Unless there is are no characters for this account, this shouldn't happen
    c.execute('CREATE TABLE spells(spellname varchar(100), classname varchar(100), dicecount int, dice int, details varchar(500))')
    conn.commit()
    chars = c.execute('select * from spells;')


print "Content-type: text/html"
print

print'''

<html>
<head><h1>Spells</h1></head>
<body>
'''
for row in chars:
    print "<br>"
    print "<br>"
    print "Spellname: "+row[0]
    print "<br>"
    print "Classes and Spell level: "+row[1]
    print "<br>"
    print "Number of Damage Dice: "+str(row[2])
    print "<br>"
    print "Sides per Dice: "+str(row[3])
    print "<br>"
    print "Further details- "+row[4]

print "<br>"
print "<br>"
print "<form method = 'post' action = 'account_page1.py'>"
print "<input type = 'submit' value = 'User Page' >"
print "</form>"

print "</body>"
print "</html>"
