"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
import os
import socket

#Open the file mbox-short.txt 
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

file = getFileHandle()

Count = 0
#Reading the file line by line
for line in file:

    #Finding lines that starts with "From"
    if not line.startswith("From"):
        continue

    #Making sure to not include the lines that start with "From:"
    if line.startswith("From:"):
        continue
    
    else:
        #Parsing the lines that starts with "From"
        list = line.split()

        #Printing the second word in the line
        print(list[1])

        #Keeping a count
        Count += 1

#Priting out count at the end
print("There were " + str(Count) + " lines in the file with From as the first word")

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com