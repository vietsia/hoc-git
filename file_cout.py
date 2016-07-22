# Use the file name mbox-short.txt as the file name

fname = raw_input("Enter file name: ")
if len(fname)==0:
   fname='mbox-short.txt'
cout=0
a=0
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
    cout=cout+1
    
    a=a+z
print cout
print a
print 'Trung binh cong la:',a/cout
