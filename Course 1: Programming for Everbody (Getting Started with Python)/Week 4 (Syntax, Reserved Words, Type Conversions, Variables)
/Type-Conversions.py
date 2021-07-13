Day=20
Month=10
Year=2000

#Even when we are not type casting float, we are still typecasting int to string.
print("\nTypecast float on Day and Year")
print("I was born on " + str(float(Day)) + " " + str(Month) + " " + str((Year)))

print("\nWithout float typecast: ")
print("I was born on " + str(Day) + " " + str(Month) + " " + str((Year)))

#Down below is a string variable which we will typecast into an Integer
stringVar="5042"
print("\nType of stringVar is :")
print(type(stringVar))
print("\nValue of stringVar is :")
print(stringVar)


intVar = int(stringVar)
print("\nType of intVar is :")
print(type(intVar))
print("\nValue of intVar is :")
print(intVar)

#String to integer typecast won't work if the string wasn't comprised of numbers.






"""
Output:


Typecast float on Day and Year
I was born on 20.0 10 2000

Without float typecast: 
I was born on 20 10 2000

Type of stringVar is :
<class 'str'>

Value of stringVar is :
5042

Type of intVar is :
<class 'int'>

Value of intVar is :
5042

"""