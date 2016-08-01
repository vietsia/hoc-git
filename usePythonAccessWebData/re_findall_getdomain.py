import re
fname=open('mbox-short.txt')
count=0
for line in fname:
    line.rstrip()
    if not line.startswith('From:'): continue
    y=re.findall('@([^ ]*)',line)
    count=count+1
    print y
print count
