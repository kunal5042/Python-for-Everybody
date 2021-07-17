"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

Desired output:
Average spam confidence: 0.7507185185185187
"""
import os
import socket

def getFileHandle():
    try:
        fileName = input("Please enter a file's name:\n")
        file = open(fileName)
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

file = getFileHandle()

lineCount = 0
totalConfidence = 0.0

for line in file:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lineCount += 1
    index = line.find('0')
    try:
        totalConfidence += float((line[index:]).strip())
    except:
        print("Error while parsing the string.")

print("Average spam confidence: " + str(totalConfidence / lineCount))

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com