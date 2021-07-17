#Python has built-in support for TCP Sockets

import socket
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #Host         #Port
mySock.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/words.txt HTTP/1.0\r\n\r\n'.encode()

mySock.send(cmd)

while True:
    data = mySock.recv(5042)
    if (len(data)<1):
        break
    print(data.decode())

mySock.close()

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com