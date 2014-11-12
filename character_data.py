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
<script src="jquery.js"></script>
<script type="text/javascript">
function showcharacter(str){
    $.ajax(
      {
        url: "cgi-bin/cresponse.py",
        type: "POST",
        data: str,
        dataType: "text",
        success: function(dat) {
        var res = var.split(",");
        document.getElementById("charname").innerHTML="Character name: "+res[0];
        document.getElementById("charlvl").innerHTML="Level: "+res[1];
        document.getElementById("charstr").innerHTML="Strength: "+res[2];
        document.getElementById("chardex").innerHTML="Dexterity: "+res[3];
        document.getElementById("charcon").innerHTML="Constitution: "+res[4];
        document.getElementById("charint").innerHTML="Intelligence: "+res[5];
        document.getElementById("charwis").innerHTML="Wisdom: "+res[6];
        document.getElementById("charcha").innerHTML="Charisma: "+res[7];
        document.getElementById("charhp").innerHTML="HP: "+res[8]+"/"+res[9];

        },
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
    print "hello"
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
</body>
</html>
'''

#create ajax tool with character data that we can change
#character data wanted:character name, player name, character level, str, dex, con, int, wis, cha, hp
