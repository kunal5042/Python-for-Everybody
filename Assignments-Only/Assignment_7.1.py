"""
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""

import urllib.request, urllib.parse, urllib.error

def getFileHandle():
    try:
        fileName = input("Please enter a file's name:\n")
        file = open(fileName)
        return file
    except:
            print("\nSample data file not found.")
            print("I'll download it for you!\n\nProgram execution will continue once the sample data is available")

            fileHandle = urllib.request.urlopen('http://data.pr4e.org/words.txt')
            
            print("\nDESIRED OUTPUT:\n")
            print((fileHandle.read()).decode().upper().strip())
            quit()

file = getFileHandle()

print(((file.read()).upper()).rstrip())

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com