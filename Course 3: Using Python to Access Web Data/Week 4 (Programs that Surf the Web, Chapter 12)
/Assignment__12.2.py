import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Gabriella.html'
print("URL: " + url)

choice = input("\nEnter 1 to change the url\nEnter 2 to continue\n")
try:
    if int(choice) == 1:
        url = input("Enter the new url:\n")
    elif int(choice) != 2:
        print("Invalid choice: " + str(choice))
        print("Continuing with the default url: " + str(url))
except:
    print("Invalid input: " + str(choice))
    print("Continuing with the default url: " + str(url))
try:
    Position = input("Enter the position of the link to follow:\n")
    Frequency = input("How many times to follow?\n")
    Position = int(Position) 
    Frequency = int(Frequency) + 1
    print()
except:
    print("Invalid input")
    print("Using default position as 18 and default frequency of 8")
    Frequency = 8
    Position = 18

def myFunction(url, Times):
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print("Can't open the given url\nExiting...")
        return
    
    try:
        # Read html and clean it up
        mySoup = BeautifulSoup(html, 'html.parser')
    except:
        print("Error while parsing the html data using beautiful soup.\nExiting...")
    
    index = int(Times)
    index = index - 1
    if index == 0:
        return

    count = 0
    # Returns a list
    tags = mySoup('a')
    for tag in tags:
        count += 1
        if count == Position:
            #print('Tag: ', tag)
            print(str(Frequency - index) + ' ' + str(tag.contents[0]))
            #print('Attrs:', tag.attrs)
            myFunction((tag.get('href', None)),index)



myFunction(url, Frequency)

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com

"""
QUESTION:
Welcome Kunal from Using Python to Access Web Data

Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Gabriella.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: J
"""