#!/gadach/local/bin/python
"""this program is run when other room is not occupied and player successfully leaves scrook1. the other program calls this program"""
"""set resources.csv of scrook1 room to _,_,0 """

import csv
"""
file is erased before values can be changed. row is therefore empty when trying to rewrite
with open('resources.csv','rw') as f:
	reader = csv.reader(f)
	for row in reader:	
		row[2]='0'
	writer = csv.writer(f)
	writer.writerows(row)
f.close()	

"""

r = csv.reader(open('resources.csv')) 
lines = [l for l in r]
lines[0][2] = '0'
writer = csv.writer(open('resources.csv', 'w'))
writer.writerows(lines)
