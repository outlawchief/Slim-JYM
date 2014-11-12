#!/usr/bin/python
import cgi
import datetime
import time
import os
import Cookie
import cgitb # to facilitate debugging
import sqlite3 # database work
# Python and Gevent
from gevent.pywsgi import WSGIServer
from gevent import monkey

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

monkey.patch_all() # makes many blocking calls asynchronous

def application(environ, start_response):
    if environ["REQUEST_METHOD"]!="GET": # your JS uses post, so if it isn't post, it isn't you
        start_response("403 Forbidden", [("Content-Type", "text/html; charset=utf-8")])
        return "403 Forbidden"
    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    r = environ["wsgi.input"].read() # get the post data
    for row in c.execute('select * from characters where name = ? and user = ?',(r,username)): #Read for existing user account
        if len(row) != 0:
            return row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]

address = "character_data.py"
server = WSGIServer(address, application)
server.backlog = 256
server.serve_forever()


