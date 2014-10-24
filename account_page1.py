#!/usr/bin/python
import cgi
import datetime
import os
import Cookie
import cgitb # to facilitate debugging
import turtle #graphics 
cgitb.enable()

#This page is the first thing a user sees once logged in
	
print "Content-type: text/html"
# don't forget the extra newline!
print

if 'HTTP_COOKIE' in os.environ:
	
	cookies = os.environ['HTTP_COOKIE']
	c = Cookie.SimpleCookie()
	c.load(cookies)
	
	username = c['username'].value
	password = c['password'].value
	
	print "<html>"
	print "<head><title>Logged In Page</title></head>"
	print "<style> body {background-color: #66FF33} </style>"
	print "<body>"
	print "<h1>Hello " + username + "</h1>" #header
	print "<form>"
	print "</form>"
	print "</body>"
	print "</html>"	
else:
	print "<html>"
	print "<body>"
	print "<h1>You Must Be Logged In To View This Page</h1>"
	print "</body>"
	print "</html>"

#print "<input type= 'log out'>"

