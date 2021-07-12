"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

Desired Output
Invalid input
Maximum is 10
Minimum is 2
"""
Maximum = 0
Minimum = None
Sum     = 0
Average = 0
Count   = 0
Number  = 0

while True:
    number = input("Please enter a number\n")
    if number == 'done':
        break

    try:

        Number = int(number)
        Count += 1
        Sum += Number
        if Maximum < Number:
            Maximum = Number

        if Minimum is None:
            Minimum = Number
        
        if Minimum > Number:
            Minimum = Number

    except:

        print("Invalid input")
    
Average = Sum / Count

print("Maximum is", Maximum)
print("Minimum is", Minimum)

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com