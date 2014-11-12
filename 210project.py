#!/usr/bin/python
import cgi
import datetime
import os
import Cookie
import cgitb # to facilitate debugging
cgitb.enable()

print "Content-type: text/html"
print 

if 'HTTP_COOKIE' in os.environ:
	
	cookies = os.environ['HTTP_COOKIE']
	c = Cookie.SimpleCookie()
	c.load(cookies)
	
	username = c['username'].value
	password = c['password'].value
	print "<html>"
	print "<body>"
	print "<h1>Hello " + username +"</h1>"
	print "<form method = 'post' action = 'account_page1.py'>"
	print "<input type = 'submit' value = 'User Page' >"
	print "</form>"
	print "<form>"
	print "<button onclick='killCookie()'>Log Out</button>"
	print "<script>"
	print "function killCookie() { "
	print "document.cookie = 'password=; expires=Thu, 01 Jan 1970 00:00:00 GMT'"
	print "document.cookie = 'username=; expires=Thu, 01 Jan 1970 00:00:00 GMT' }"	
	print "</script>"
	print "</form>"
	print "</body>"
	print "</html>"

else:
	#print "Content-type: text/html"
	# don't forget the extra newline!
	#print
	print "<html>"
	print "<head><title>My webpage</title></head>"
	print "<body>"
	print "<h1>Hello TA's!</h1>" #header

	print "<form method='post' action='index.py'>" #What happens when you submit the data
	print "Username: <input type='text' name='username'>"
	print "Password: <input type='text' name='password'><br>"
	print "Remember Me: <input type='checkbox' name='rememberme' value='true'><br>"
	print "<input type= 'submit'>" # all fields are submitted to 'index.py'
	#print "<input type= 'Sign in'>"  #for when we have a sign up or log in system
	print "</form>"

	print "</body>"
	print "</html>"
