import re
fname=open('regex_sum_281890.txt')
cong=[]
for line in fname:
     line.rstrip()
     y=re.findall('[0-9]+',line)
     if len(y)<1: continue
     for z in y:
         cong.append(int(z))
print cong
print sum(cong) 

