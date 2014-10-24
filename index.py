#!/usr/bin/python
import cgi
import datetime
import time
import os
import Cookie
import cgitb # to facilitate debugging
import sqlite3 # database work

cgitb.enable()

form = cgi.FieldStorage() #variable "form" becomes a buffer array from passed in data

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

username = form.getvalue("username", None) #get variable "username" from buffer
password = form.getvalue("password", None) #get variable "password" from buffer
remembered = form.getvalue("rememberme", False) #Do we remember the session post session

#not sure if these two are correct
cookie_string = os.environ.get('HTTP_COOKIE')  # assign string username to cookie
expires = time.time() + 100 * 24 * 3600 # 100 days from now

expires = datetime.datetime(2009, 2, 14, 18, 30, 14) + datetime.timedelta(hours=1)

if username == None:
  print "Content-type: text/html"
  print # don't forget newline
  print "<html>"
  print "<body>"
  print "<h1>Please Enter a Valid Username</h1>" # user is already logged in on a different machine
  print "<form method = 'post' action = '210project.py'>"
  print "<input type = 'submit' value = 'Back to Log in Page' >"
  print "</form>"  
  print "</body>"
  print "</html>"  
else:  #---------------------------------Already logged in Error Cases-------------------------
  if cookie_string:
    cook = Cookie.SimpleCookie(cookie_string)
    if (username != cook['username'].value):
        print "Content-type: text/html"
        print # don't forget newline
        print "<html>"
        print "<body>"
        print "<h1>You are already logged in (wrong username)</h1>" # user is already logged in on a different machine
        print "</body>"
        print "</html>"
    else:
        if (password != cook['password'].value):
            print "Content-type: text/html"
            print # don't forget newline
            print "<html>"
            print "<body>"
            print "<h1>You are already logged in (Wrong password)</h1>"  #user already logged in & user enters wrong password
            print "</body>"
            print "</html>"
        else:
            print "Content-type: text/html"
            print # don't forget newline
            print "<html>"
            print "<body>"
            print "<h1>You are already logged in</h1>"   #user is already logged in
            print "</body>"
            print "</html>"
  #-----------------------------------------------------------------------------------------
  
  
  #-----------------------User not Already Logged In--------------------------------
  else:
    cook = Cookie.SimpleCookie()
    cook['username'] = username;
    cook['password'] = password;
    
    if(remembered == True):
      cook['with_max_age'] = 'expires in x minutes'
      cook['with_max_age']['max-age'] = 300000000000 # seconds
    
    c.execute('select * from users where name =?;', (username,))   # find if the username is in the database
    rows = c.fetchall() # fetch everything from database
    
    found_name = ""
    found_pass = ""
    
    for row in rows:
      if row[2] == username:
        if rows!=None:   
            print "Content-type: text/html"
            print cook
            print # don't forget newline
            print "<html>"
            print "<body>"
            print "<h1>Welcome back " + username + "</h1>" # Returning User
            print "</body>"
            print "</html>"        
        else:
            print "Content-type: text/html"
            print # don't forget newline
            print "<html>"
            print "<body>"
            print "<h1>Error: imposter wrong password</h1>"  #--------Incorrect Password
            print "</body>"
            print "</html>"
    else:
      try:
        c.execute('update users set name=? where pass=?', (username, password))
        conn.commit()
        print "Content-type: text/html"
        print "Status: 303 See other"
        print "Location: account_page1.py"         
        print cook
        print # don't forget newline   
        print "<html>"
        print "<body>"
        for row in rows:
          print row
        print "<h1>Welcome " + username + "</h1>"  # First time user
        print "</body>"
        print "</html>"
      except sqlite3.OperationalError:   #if table does not exist create table (should never run)
        c.execute('create table users(name varchar(100) primary key, pass varchar(100));')
        c.execute('update users set name=? where pass=?', (username, password))
        conn.commit()
        print "Content-type: text/html"
        print cook
        print # don't forget newline
        print "<html>"
        print "<body>"
        print "<h1>Welcome " + username + " created new table</h1>"
        print "</body>"
        print "</html>"
 