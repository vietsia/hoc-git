# Use the file name mbox-short.txt as the file name

fname = raw_input("Enter file name: ")
congdon=[]
if len(fname)==0:
   fname='mbox-short.txt'
try:
   fh = open(fname)
except:
   print 'Can not open the file',fname
   exit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x=line.find('0')
    y=line[x: ]
    z=float(y)
    congdon.append(z)

print sum(congdon)
print len(congdon)
print 'Trung binh cong la:',sum(congdon)/len(congdon)

