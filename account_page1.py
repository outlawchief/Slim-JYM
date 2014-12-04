#!/usr/bin/python
import cgi
import datetime
import os
import Cookie
import cgitb # to facilitate debugging
import turtle #graphics
import sqlite3 # database work
cgitb.enable()

#This page is the first thing a user sees once logged in

#---------Connect to Database-------
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
#-----------------------------------

#-----------Header---------------------
print "Content-type: text/html"
# don't forget the extra newline!
print
#--------------------------------------

def get_users():
	c.execute("SELECT * FROM users")
	print(c.fetchall())

get_users()

if 'HTTP_COOKIE' in os.environ:

	cookies = os.environ['HTTP_COOKIE']
	cook = Cookie.SimpleCookie()
	cook.load(cookies)

	username = cook['username'].value
	password = cook['password'].value


	print "<html>"
	print "<head><title>Logged In Page</title></head>"
	print "<body>"
	print "<h1>Hello " + username + "</h1>" #header
	print "<h5>User Bio </h5>"
	print "<textarea name='paragraph_text' cols='50' rows='10'></textarea>" # User Bio Paragraph
	print "<form method = 'post' action = 'account_page1.py'>"
	print "<button onclick='save()'>Save Bio</button>"

	print "</br>"

	#Log out button, redirects to home page
	print "<form method = 'post' action = '210project.py'>"
	print "<button onclick='killCookie()'>Log Out</button>"
	print "</form>"

	#Delete account button
	#So here's the problem, I don't really know how to make a python database call
	#in the middle of an html database such that when the button is clicked, a function is called that will
	#make a database call to delete the database. Since I only need the name, I am using the text box as
	#a sort of workaround. The only other way is to use something called Flask or maybe AJAX
	print'''
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	<script type="text/javascript">
	function del(name) {
		$.ajax({
			url: "delete.py",
			data: {param: name },
			type: "POST",
			success: function(dat) {
				alert("SUCCESS")
			},
			error: function(html){
				alert("ERROR");
			},
		}).done(function(o) {

		});

	}
	</script>
	'''
	
	print "<form method = 'get' action = 'account_page1.py'>"
	print "<button onclick='del("+username+")'>Delete</button>"
	print "</form>"
	
	print "<form method = 'post' action = 'creature_create.py'>"
	print "<button>Make A New Character</button>"
	print "</form>"

	print "<form method = 'post' action = 'character_data.py'>"
	print "<button>Access Your Characters</button>"
	print "</form>"

	print "<form method = 'post' action = 'spell_create.py'>"
	print "<button>Design a spell</button>"
	print "</form>"

	print "<form method = 'post' action = 'spells.py'>"
	print "<button>View all spells</button>"
	print "</form>"

	#Java script
	print "<script>"
	# -----------------Log out function --------------
	print "function killCookie() { "
	print "document.cookie = 'password=; expires=Thu, 01 Jan 1970 00:00:00 GMT'"
	print "document.cookie = 'username=; expires=Thu, 01 Jan 1970 00:00:00 GMT' }"
	#------------------Text Save Function-------------------
	print "function save(){"
	print "var text_to_save=document.getElementById('paragraph_text').value;"
	print "localStorage.setItem('text', text_to_save); // save the item?"
	print "}"
	print "</script>"
	#------------------Delete Function---------------	
	
	print ""
	print "</body>"
	print "</html>"
else:
	#User not logged in case
	print "<html>"
	print "<body>"
	print "<h1>You Must Be Logged In To View This Page</h1>"
	print "<form method = 'post' action = '210project.py'>"
	print "<button>Log Out</button>"
	print "</form>"
	print "</body>"
	print "</html>"

#print "<input type= 'log out'>"
