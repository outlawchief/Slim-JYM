



import cgi
import datetime
import os
cookie_string = os.environ.get('HTTP_COOKIE')
import Cookie
import cgitb # to facilitate debugging
cgitb.enable()

form = cgi.FieldStorage()


print "Content-type: text/html"
# don't forget the extra newline!
print

print "<html>"
print "<head><title>My webpage</title></head>"
print "<body>"
print "<h1>Hello TA's!</h1>"
print "<h2>Your name is: " + form['my_name'].value + "</h2>"
print "<h2>Email: " + form['my_age'].value + "</h2>"
print "<button type=button>" + Submit + "</button>"

print "</body>"
print "</html>"
