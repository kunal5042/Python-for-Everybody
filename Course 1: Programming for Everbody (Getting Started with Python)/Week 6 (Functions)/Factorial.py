# Here I am using recursion to solve this problem, don't worry about it if it's your first time at recursion.

def Factorial(variable):
    if variable == 0:
        return 1
    
    return (variable * Factorial(variable-1))



variable = input("Enter a number to calculate it's factorial.\n")

try:
    x = int(variable)
except:
    print("Not a valid number.")
    x = 0

if x == 0:
    print("\nFactorial of", variable + " equals:")
    print("Cannot compute factorial, because the number you entered is invalid.")
else:
    print("\nFactorial of", variable + " equals:")
    print(Factorial(x))



