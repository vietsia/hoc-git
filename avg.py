# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x=line.find('0')
    y=line[x: ]
    z=float(y)
    print avg(z)
