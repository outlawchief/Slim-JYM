import cgi
import datetime
import os
import Cookie
import cgitb # to facilitate debugging
import turtle #graphics
import sqlite3 # database work

cgitb.enable()
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

print

input = cgi.FieldStorage()
output = input.getvalue("param", None)

q  = "delete from users where name ='%s' " %output.strip()
c.execute(q)
conn.commit()
