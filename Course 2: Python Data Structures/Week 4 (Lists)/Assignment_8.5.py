"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

#Open the file mbox-short.txt 
file = open("mbox-short.txt")

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