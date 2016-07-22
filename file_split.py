fhand=open('mbox-short.txt')
for line in fhand:
	line=line.rstrip()
	if not line.startswith('From'):continue
	w=line.split()
	email=w[1]
	print email
	name=email.split('@')
	print 'ten la:',name[0]
