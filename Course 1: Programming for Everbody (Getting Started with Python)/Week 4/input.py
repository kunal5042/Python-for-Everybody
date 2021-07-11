# A program to demonstrate input function in python.

name = input("Please enter your name: \n")
print("Welcome, " + name)

age = input("\nHow old are you?\n")

if int(age) >= 18:
    print("You are elegibile!")
else:
    remainingYears= 18 - int(age)
    print("Don't worry, you will be elegibile in less than " + str(remainingYears) + " years.")






"""
Output: When the user is less than 18 years old
Please enter your name: 
Muskan
Welcome, Muskan

How old are you?
11
Don't worry, you will be elegibile in less than 7 years.





Output: When the user is greater than 18 years old
Please enter your name: 
Kunal
Welcome, Kunal

How old are you?
20
You are elegibile!

"""