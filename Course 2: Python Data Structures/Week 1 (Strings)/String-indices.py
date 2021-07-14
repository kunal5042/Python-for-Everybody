stringVar = "KUNAL WADHWA"
stringLenght = 12
index = 0

print("Using while loop:")
while index < stringLenght:
    print("Index: " + str(index) + " \t= " + str(stringVar[index]))
    index += 1

#Using while loop
index = 0

print("\nUsing for loop:")
for letter in stringVar:
    print("Index: " + str(index) + " \t= " + str(stringVar[index]))
    index += 1

#Demo of len function in python
print("\nLenght of the string = " + str(len(stringVar)))

"""
Output:
Using while loop:
Index: 0 	= K
Index: 1 	= U
Index: 2 	= N
Index: 3 	= A
Index: 4 	= L
Index: 5 	=  
Index: 6 	= W
Index: 7 	= A
Index: 8 	= D
Index: 9 	= H
Index: 10 	= W
Index: 11 	= A

Using for loop:
Index: 0 	= K
Index: 1 	= U
Index: 2 	= N
Index: 3 	= A
Index: 4 	= L
Index: 5 	=  
Index: 6 	= W
Index: 7 	= A
Index: 8 	= D
Index: 9 	= H
Index: 10 	= W
Index: 11 	= A

Lenght of the string = 12
"""