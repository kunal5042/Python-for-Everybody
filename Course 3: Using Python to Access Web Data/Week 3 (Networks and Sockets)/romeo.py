import socket
import os

#Create a new socket to connect to the web
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to the host data.pr4e.org on port 80
mySock.connect(('data.pr4e.org',80))

#GET command for the file we seek.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

#On successful connection with the server, send the request.
mySock.send(cmd)

#Get the current directory
directory = os.getcwd()
#New file's directory
filepath = directory + '/kunal-romeo.txt'

#Create a new text file to put the received data into.
file = open(filepath, 'w+')


flag = True
#While the received data's length greater than 1
while True:

    #Keep receiving data
    data = mySock.recv(1024)
    
    #Break if length's less than 1
    if (len(data)<1):
        break

    #Runs only once
    if flag:
        string = data.decode()
        index = string.find('Content-Type: text/plain')
        index = index + len('Content-Type: text/plain')
        string = string[index:]
        file.write(string)

    #Runs only once, to take care of info received from the server which we don't need in our file.
    if flag:
        flag = False
        continue

    else:
        #Runs till the loop is stopped
        #Keep writing the data to the file
        file.write(data.decode())
        
# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com