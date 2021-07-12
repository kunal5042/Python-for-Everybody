"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
"""

score = input("Please enter a score between 0.0 and 1.0.\n")

try:
    S = float(score)
except:
    print("Not a valid number.")

if S > 1.0 or S < 0:
    print("The score is out of range.")
else:
    if S >= 0.9:
        grade = "A"
    elif S >= 0.8:
        grade = "B"
    elif S >= 0.7:
        grade = "C"
    elif S >= 0.6:
        grade = "D"
    else:
        grade = "F"

try:
    print(grade)
except:
    print("Couldn't compute grade, because either the score wasn't valid or it was out of range.")


"""
Input: 0.85

Desired Output:
B
"""
# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com