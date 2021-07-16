"""
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
"""

#print("This program computes gross pay.\n")
hours = input("Enter the number of hours:\n")
try:
    H = float(hours)
except:
    print("Not a valid number.")
    print("Default hours value is 1 and will be used.")
    H = 1

hourlyRate = input("Enter the hourly rate:\n")
try:
    HR = float(hourlyRate)
except:
    print("Not a valid number.")
    print("Default hourly rate value is 1 and will be used.")
    HR = 1

if H > 40:
    extraHours = H - 40
    print( 40*HR + (extraHours*1.5*HR))
else:
    print(HR*H)

"""
Input:
Hours = 45
Rate  = 10.05

Desired Output:
498.75
"""
# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com