"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""
import os
import socket

#Opened file
def getFileHandle():
    try:
        file = open("romeo.txt")
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
        cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

        #On successful connection with the server, send the request.
        mySock.send(cmd)

        #Get the current directory
        directory = os.getcwd()
        #New file's directory
        filepath = directory + '/romeo.txt'

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

builtList = list()

#Reading it line by line
for line in file:

    #For each word in each line
    for eachWord in line.strip().split():
        
        if eachWord in builtList:
            #Checking if the word is already in the list
            continue
        else:
        #If not, appending it to the list
            builtList.append(eachWord)

#Sorting the final list
builtList.sort()

#Printing the result
print(builtList)

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com