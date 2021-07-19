"""
USING URLLIB IN PYTHON
Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file.
"""

import urllib.request, urllib.parse, urllib.error

fileHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fileHandle:
    print(line.decode().strip())