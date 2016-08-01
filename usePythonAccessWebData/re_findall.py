import re
hand =open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    if len(y)<1: continue
    print y

