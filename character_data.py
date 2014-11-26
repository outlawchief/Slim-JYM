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
    chars = c.execute('select * from characters where user = ?',(username,))
except sqlite3.OperationalError:
    c.execute('CREATE TABLE characters(user varchar(100), name varchar(100),  lvl int, str int, dex int, con int, intel int, wis int, cha int, hp int, hpc int)')
    conn.commit()
    chars = c.execute('select * from characters where user = ?',(username,))
print "Content-type: text/html"
print

print'''

<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js">
</script>
<script type="text/javascript">
function showcharacter(str){
    $.ajax(
      {
        url: "cresponse.py",
        type: "POST",
        data: {param: str},
        dataType: "json",
        success: function(dat) { 
		console.log(dat);
		console.log(dat.name);
		console.log(dat.lvl);
        document.getElementById("charname").innerHTML="Character name: " + dat.name;
        document.getElementById("charlvl").innerHTML="Level: "+dat.lvl;
        document.getElementById("charstr").innerHTML="Strength: "+dat.str;
        document.getElementById("chardex").innerHTML="Dexterity: "+ dat.dex;
        document.getElementById("charcon").innerHTML="Constitution: "+ dat.con;
        document.getElementById("charint").innerHTML="Intelligence: "+ dat.int;
        document.getElementById("charwis").innerHTML="Wisdom: "+dat.wis;
        document.getElementById("charcha").innerHTML="Charisma: "+ dat.chr;
        document.getElementById("charhp").innerHTML="HP: "+dat.hpc+"/"+ dat.hp;
        
        },
        
        error: function(html){
          alert("ERROR");
        }
      }
    );
  };

</script>
<body>
<form action = ''>
<select name = 'characters' onchange='showcharacter(this.value)'>
<option value=''>Select a character:</option>
'''
for row in chars:
    print row
    print "<option value='",row[1],"'>",row[1],"</option>"
print '''
</select>
</form>
<br>
<div id="charname">Character name:</div>
<div id="charlvl">Level:</div>
<div id="charstr">Strength:</div>
<div id="chardex">Dexterity:</div>
<div id="charcon">Constitution:</div>
<div id="charint">Intelligence:</div>
<div id="charwis">Wisdom:</div>
<div id="charcha">Charisma:</div>
<div id="charhp">HP: /</div>
'''
for row in chars:
    print row[0]
print "</body>"
print "</html>"

#create ajax tool with character data that we can change
#character data wanted:character name, player name, character level, str, dex, con, int, wis, cha, hp
