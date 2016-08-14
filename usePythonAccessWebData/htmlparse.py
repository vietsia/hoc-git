import urllib
import re
from BeautifulSoup import *
url=raw_input('Enter- ')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)
list=[]
tags=soup('span')
for tag in tags:
     z=str(tag)
     y=re.findall('[0-9]+',z)
     for x in y:
         list.append(int(x))
print list
print sum(list)

