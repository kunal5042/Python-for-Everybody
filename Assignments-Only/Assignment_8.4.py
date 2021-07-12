"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""
#Opened file
file = open("romeo.txt")

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