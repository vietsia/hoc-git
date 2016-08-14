import re
fname=open('mbox-short.txt')
count=0
for line in fname:
    line.rstrip()
    y=re.findall('^From: .*@([^ ]*)',line)
    if len(y)<1: continue
    count=count+1
    print y
print count
