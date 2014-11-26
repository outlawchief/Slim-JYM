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
except sqlite3.OperationalError: #Unless there is are no characters for this account, this shouldn't happen
    c.execute('CREATE TABLE characters(user varchar(100), name varchar(100),  lvl int, str int, dex int, con int, intel int, wis int, cha int, hp int, hpc int)')
    conn.commit()
    chars = c.execute('select * from characters where user = ?',(username,))


print "Content-type: text/html"
print

print'''

<html>
<head><h1>Characters Page</h1></head>
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

#Delete character function, takes in character name in text box, reads, then deletes from database
print'''
<br>
<form name = "del" method = 'get' action = '/cgi-bin/character_data.py'>
Character name:<br> <input type="text" name="c_name">
<input type="submit" value="Delete">
</form>
'''
form = cgi.FieldStorage()
name = form.getvalue('c_name')
q  = "delete from characters where name ='%s' " % name
c.execute(q)
conn.commit()

print'''
<br>
<form name = "hpup1" method = 'get' action = '/cgi-bin/character_data.py'>
Character name:<br> <input type="text" name="1_name">
<input type="submit" value="Increase HP by 1">
</form>
'''
form = cgi.FieldStorage()
name1 = form.getvalue('1_name')
hp  = "update characters set hp=hp+1 where name ='%s' " % name1
c.execute(hp)
conn.commit()

print'''
<br>
<form name = "hpup5" method = 'get' action = '/cgi-bin/character_data.py'>
Character name:<br> <input type="text" name="5_name">
<input type="submit" value="Increase HP by 5">
</form>
'''
form = cgi.FieldStorage()
name5 = form.getvalue('5_name')
hp  = "update characters set hp=hp+5 where name ='%s' " % name5
c.execute(hp)
conn.commit()

print'''
<br>
<form name = "hpup-1" method = 'get' action = '/cgi-bin/character_data.py'>
Character name:<br> <input type="text" name="-1_name">
<input type="submit" value="Lower HP by 1">
</form>
'''
form = cgi.FieldStorage()
name01 = form.getvalue('-1_name')
hp  = "update characters set hp=hp-1 where name ='%s' " % name01
c.execute(hp)
conn.commit()

print'''
<br>
<form name = "hpup-5" method = 'get' action = '/cgi-bin/character_data.py'>
Character name:<br> <input type="text" name="-5_name">
<input type="submit" value="Lower HP by 5">
</form>
'''
form = cgi.FieldStorage()
name05 = form.getvalue('-5_name')
hp  = "update characters set hp=hp-5 where name ='%s' " % name05
c.execute(hp)
conn.commit()

print "<br>"
print "<form method = 'post' action = 'account_page1.py'>"
print "<input type = 'submit' value = 'User Page' >"
print "</form>"

print "</body>"
print "</html>"

#create ajax tool with character data that we can change
#character data wanted:character name, player name, character level, str, dex, con, int, wis, cha, hp
