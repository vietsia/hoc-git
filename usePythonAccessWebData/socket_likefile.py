import urllib
fhand=urllib.urlopen('http://dantri.com.vn/su-kien/tho-nhi-ky-thay-mau-quan-doi-20160802110514938.htm')
for line in fhand:
    print line.rstrip()

