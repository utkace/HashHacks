import sqlite3
import json
import sys
a=''
s=1
db=sqlite3.connect('details')
cur=db.cursor()
name=""
cur.execute('SELECT id, cid, rid, uid, expert, text from reviews where cid = ?',(str(sys.argv[1]),))
ab=cur.fetchall()
#print (ab)
r=0
s=0
D={}
for i in ab:
	a = ''
	for t in i:
		r+=1
		a+=str(t)
		a+='#'
	D[s]=a
	s+=1
#print (rev_list)

print (json.dumps(D))
sys.exit()