"""

9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

Desired Output
cwen@iupui.edu 5

"""
import os
import socket

def getFileHandle():
    try:
        file = open("mbox-short.txt")
        return file
    except:
        directory = os.getcwd()
        print("\nSample data file not found.")
        print("I'll download it for you!\n\nProgram execution will continue once the sample data is available")
        
        #Create a new socket to connect to the web
        mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Connect to the host data.pr4e.org on port 80
        mySock.connect(('data.pr4e.org',80))

        #GET command for the file we seek.
        cmd = 'GET http://data.pr4e.org/mbox-short.txt HTTP/1.0\r\n\r\n'.encode()

        #On successful connection with the server, send the request.
        mySock.send(cmd)

        #Get the current directory
        directory = os.getcwd()
        #New file's directory
        filepath = directory + '/mbox-short.txt'

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
        print("Done\n\n")
        file.seek(0)
        return file

def createEmailDictionary():
    
    sendersEmail = dict()
    for line in getFileHandle():
        if not line.startswith("From"):
            continue
    
        if line.startswith("From"):
            if line.startswith("From:"):
                continue
            else:
                list = line.split()
                sendersEmail[list[1]] = sendersEmail.get((list[1].strip()), 0) + 1
    return sendersEmail

def extractPC_fromEmailDict():
    maxValue = None
    maxKey   = None
    for key, value in createEmailDictionary().items():
        if maxValue is None or maxValue < value:
            maxValue = value
            maxKey   = key
    return maxKey, maxValue


prolificCommiterKey, prolificCommiterValue = extractPC_fromEmailDict()
print(prolificCommiterKey + " " + str(prolificCommiterValue))

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com