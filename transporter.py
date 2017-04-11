#!/usr/bin/python
#called by NESW of other room
#recall that information about room inventory and capacity is in inventory.csv

import cgi
import csv
import re


#Successful entrance. Add player's resources (with manna-1) in the playerInventory hidden tag. 
def success():
	
	print"Content-type: text/html\n\n"
	form = cgi.FieldStorage()
	inventory = form.getvalue('inventory')

	#change occupied value in this room to 1 (full)
	r = csv.reader(open('resources.csv'))
	lines = [l for l in r]
	lines[0][2] = '1'
	writer = csv.writer(open('resources.csv','w'))
	writer.writerows(lines)
	
	#subtract 1 manna from player
	invArr = re.findall('\d+',inventory)
	manna = int(invArr[0])-1
	gold = int(invArr[1])
	inventory = "%d,%d" %(manna, gold) 
	inven = '"%s"' %inventory

	if manna<=0:
		print "OUT OF MANNA. GAME OVER"
	else:
		print '''
			<html>
			<title> Stewart Bio </title>
			<body> 
			<center>
			<h1>Your Inventory: Manna = ''',manna,'''Gold =''',gold,'''</h1>
			<img src ="https://mpsapsiblog.files.wordpress.com/2015/11/7u.jpg" width="900" height="600">
			</br>
			<font>To go to class, type PLAY.</font></br>
			<form action="http://cs.mcgill.ca/~gadach/cgi-bin/room.cgi" method="post">
			<input type ="text" name="input">
			<input type = "submit" value="Submit"></br>
			<input type="hidden" name="inventory" value=''',inven,'''> 
			<font> Other options: DROP, EXIT, REFRESH </font></br>
			</form>
			<form style= "display:inline;" action="http://cs.mcgill.ca/~gadach/cgi-bin/transporter.py" method="post">
			<input type = "hidden" name = "inventory" value = ''',inven,'''>
			<input type = "submit" value = "North">
			</form> </br>
			<form style= "display:inline;" action="http://cs.mcgill.ca/~gadach/cgi-bin/transporter.py" method="post">
			<input type = "hidden" name = "inventory" value = ''',inven,'''>	
			<input type = "submit" value = "West">
			</form> 
			<img src ="http://biology.mcgill.ca/building/stewart_photos/Building.jpg" width="300" height="200">
			<form style= "display:inline;" action="http://cs.mcgill.ca/~gadach/cgi-bin/transporter.py" method="post">
			<input type = "submit" value = "East">
			<input type = "hidden" name = "inventory" value = ''',inven,'''>
			</form></br>
			<form style= "display:inline;" action="http://cs.mcgill.ca/~jmesich/cgi-bin/transporter.py" method="post">
			<input type = "submit" value = "South">
			<input type = "hidden" name = "inventory" value = ''',inven,'''>
			</form>
			</center>
			</body></html>
			''',

	#run other room's success.py 

#send user back to other room through REFRESH
def failure():

	#send the player back to their room by passing post request with REFRESH
	url = form.getvalue('URL')
	values = {'input' : 'REFRESH', 'inventory' : form.getvalue('inventory') }
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()



#getting occupied value: read csv file and use boolean"""
#format of our csv file: manna,gold,occupied"""

with open('resources.csv','r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		row = row

	if (row[2]=="0"):
	#if my room occupied value is 0 (empty) then run success() and success.py of other room"""
		success()
		#url = 'https://cs.mcgill.ca/~scrook1/a4/success.py'
		#values = {'inventory' : 'inventory')
	else:
	#if room occupied value is 1 (full) then run room.c of other room using refresh input"""
		failure()

csvfile.close()
