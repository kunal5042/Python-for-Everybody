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
