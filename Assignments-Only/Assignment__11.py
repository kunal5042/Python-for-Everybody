#Import regex library
import re

def getFileHandle():
    fileName = input("Please enter the name of the file to operate on\n")
    try:
        file = open(fileName, "r")
        return file
    except:
        print()
        print("Could not open the file, exiting\n")
        quit()

def extractNumSum(file):
    #findall returns a list of matching strings.
    #[0-9] will match any numbers between 0 and 9, and + will look for more following numbers one or more times.
    list = re.findall("[0-9]+", file.read())
    
    sum = 0
    for number in list:
        sum += int(number)
    

    return sum

print(extractNumSum(getFileHandle()))

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com