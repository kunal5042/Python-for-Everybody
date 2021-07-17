#Python has built-in support for TCP Sockets

import socket
import os

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #Host         #Port
mySock.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/mbox-short.txt HTTP/1.0\r\n\r\n'.encode()

mySock.send(cmd)

list = []
count = 1
while True:
    data = mySock.recv(1024)
    
    if (len(data)<1):
        break

    if count == 1:
        string = data.decode()
        flag = False
        x = 1
        for str in string.split():
            if x == 1:
                if not str.startswith('text/plain'):
                    flag = False
                else:
                    x = 2
                    flag = True
            if flag:
                if str == 'text/plain':
                    continue
                else:
                    list.append(str)
    
    if count == 1:
        count = 2
        continue
    else:
        list.append(data.decode())

directory = os.getcwd()
filepath = directory + '/romeo.txt'

file = open(filepath, 'w+')

for element in list:
    string = (element + " ")
    file.write(string)

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com