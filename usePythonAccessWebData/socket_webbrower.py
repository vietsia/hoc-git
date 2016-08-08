import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.dantri.com.vn',80))
mysock.send('GET http://dantri.com.vn/su-kien/bao-lon-co-the-thoi-bay-dao-nhan-tao-trung-quoc-boi-dap-trai-phep-o-bien-dong-20160802064957598.htm HTTP/1.0 \n\n')
while True:
     data=mysock.recv(512)
     if (len(data)<1): break
     print data
mysock.close()
