"""Write a program to read through the mbox-short.txt and 
figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer"""
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
    counts[y]=counts.get(y,0)+1 
bigcount=None
bigword=None
for a,b in counts.items():
    if bigcount==None or b>bigcount:
        bigcount=b
        bigword=a
print bigword, bigcount

    

