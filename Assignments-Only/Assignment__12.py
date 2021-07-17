#Need it to create a socket
import socket

#Creating a socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting to given host on given port
mySocket.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

#On successful connection, sending the request to the host server.
mySocket.send(cmd)

while True:

    #Retreivng encoded bytes of data from server
    data = mySocket.recv(1024)
    
    #To stop the loop
    if (len(data)<1):
        break

    #Printing the data after decoding
    print(data.decode())

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com