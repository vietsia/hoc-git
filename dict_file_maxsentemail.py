name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
list=[]
counts=dict()
for line in handle:
    line.rstrip()
    if not line.startswith('From:'): continue
    words=line.split()
    x= words[1]
    list.append(x)
for y in list:
    counts[y]=counts.get(y,0) + 1
for key in counts:
    z=counts.values() 
    if counts[key]==max(z):
        print key, max(z)

