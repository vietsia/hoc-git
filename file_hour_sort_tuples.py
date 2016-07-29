'''Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
list=[]
counts=dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    words=line.split()
    x=words[5]
    y=x.split(":")
    z=y[0]
    list.append(z)
for a in list:
    counts[a]=counts.get(a,0) + 1
for b,c in sorted(counts.items()):
   print b,c
