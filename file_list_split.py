#thu phat choi coi
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
   fh = open(fname)
except:
   print "File nay khong dung", fh
count = 0
for line in fh:
    if not line.startswith('From:'): continue
    cu=line.split()
    email= cu[1]
    print email
    count=count+1
print "There were", count, "lines in the file with From as the first word"

