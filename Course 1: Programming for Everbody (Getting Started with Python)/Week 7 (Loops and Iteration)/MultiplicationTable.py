def MultiplicationTable(number, range):
    index = 1
    while index <= range:
        print(str(number) + " x " +  str(index) + "\t = " + str(number * index))
        index = index + 1

def checkInput_And_printTable(number, range):
    try:
        x = float(number)
        y = float(range)
        print("Requested table:")
        MultiplicationTable(x, y)
    except:
        print("Invalid input!")

number = input("Enter a number to print it's multiplication table.\n")

range = input("Enter the range of the multiplication table.\n")

checkInput_And_printTable(number, range)
