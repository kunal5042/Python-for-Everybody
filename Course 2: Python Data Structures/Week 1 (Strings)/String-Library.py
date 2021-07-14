"""
Python has a nyumber of string fucntions which are in the string libraray.

These functions are alraedy build into every string - we invoke them by appending the function to the string variable.

These functions do not modify the original string, instead they return a new string that has been altered.
"""

s = "bbbbbb    AAAAAA        "

print(s.lower())

print("THIS IS LOWERCASE".lower())
print("this is upercase!".upper())
       
#print(type(s))
#dir shows the functions that are available for type
#print(dir(s))

#Common ones for string.
#print(s.capitalize())

print(s.swapcase())

print(s [ s.find('nal') : (s.find('nal')+3) ] )

print( s.replace('nal', 'NAAAAAAAAAAAALLLLLLL'))

print( s.strip())
# lstrip() rstrip()

print( s.startswith('KUNA'))

data = "From kunalwadhwa.cs@gmail.com Mon Jul 12 01:11:11 2021"
print("Input\t: " + data)
atPosition = data.find('k')
#print(atPosition)

spacePosition = data.find('@')
#print(spacePosition)

sender = data[(atPosition): spacePosition]
print("Sender\t: " + sender)

"""
Output:

bbbbbb    aaaaaa        
this is lowercase
THIS IS UPERCASE!
BBBBBB    aaaaaa        

bbbbbb    AAAAAA        
bbbbbb    AAAAAA
False
Input	: From kunalwadhwa.cs@gmail.com Mon Jul 12 01:11:11 2021
Sender	: kunalwadhwa.cs

"""