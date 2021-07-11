#Demonstration of try and except in python

print("This program will multiply two user entered numbers.")

num1 = input("Please enter number 1\n")

try:
    x = int(num1)
except:
    print("Not a valid number.")
    print("I'll assume this number to be 5042 in that case.")
    x = 5042

num2 = input("\nPlease enter number 2\n")

try:
    y = int(num2)
except:
    print("Not a valid number.")
    print("I'll assume this number to be 5042 in that case.")
    y = 5042

print("The multiplication result is: " + str(x*y))