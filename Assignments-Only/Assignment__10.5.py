"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

Desired Output:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

#Creates a file handle and returns it.
def getFileHandle():
    try:
        #Open file
        file = open("mbox-short.txt")
        return file
    except:
        #If file is not present, provides a link from where it can be downloaded.
        print()
        print("Please follow this link -> https://www.py4e.com/code3/mbox-short.txt\nAnd download the data from there and save it as mbox-short.txt in the same directory.\nAs this program operates on that data, it won't work unless that data has been fed to it.")
        file = None
        #Stops execution, because the rest of the program can't work without the file and it's data.
        quit()


#Creates a list of required lines for parsing.
def getList(file):

    #Empty list initialization
    list = []

    #For each line in the file
    for line in file:
        #Find the desired line
        if not line.startswith("From"):
            continue

        if line.startswith("From"):

            #Ignore corner cases 
            if line.startswith("From:"):
                continue
            else:

                #Add the found line to the list
                list.append(line)
    
    #Return the list parsing.
    return list



#Creates a dictionary of time and it's frequency from the list.
def getTimeDict(list):

    #Initialization of an empty dictionary
    TimeDict = {}

    for line in list:
        #Split the line and make a list out of it.
        line = line.split()

        #Take the index 5 which is our time and remove the rest.
        line = line[5]

        #Check for the time key in dictionary
        #If not present, create a new key with value 1
        #If found, increment it's value by 1
        TimeDict[line[0:2]] = TimeDict.get(line[0:2],0) + 1
    

    #Return the dictionary
    return TimeDict



#Sorts a dictionary, and returns it as a list of tuples, where each tuples is 2 elements
def getSortedList(TimeDict):
    
    #Using list-comprehension in python
    requiredList = sorted([(key, value) for key, value in TimeDict.items()])
    return requiredList


#Getting desired output
for key, value in getSortedList(getTimeDict(getList(getFileHandle()))):
    print(key, value)


# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com