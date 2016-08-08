import sqlite3
conn=sqlite3.connect('testdb.sqlite')
cur=conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts(org TEXT, count INTERGER)''')
fname=raw_input('Enter file name: ')
if(len(fname)<1): fname='mbox.txt'
list=[]
cat=dict()
fh=open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    a=line.split()
    email=a[1]
    b=email.split('@')
    org=b[1]
    list.append(org)
for y in list:
    cat[y]=cat.get(y,0)+1
for a,b in sorted(cat.items()):
    cur.execute('''INSERT INTO Counts(org,count) VALUES(?,?)''',(a,b))
    conn.commit()
row = cur.fetchone()
for row in cur.execute('''SELECT org,count FROM Counts ORDER BY count DESC'''):
    print str(row[0]), row[1]
cur.close() 

   


