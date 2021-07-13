iterable = 2
while True:
    print()
    print("Multiplied by 2: " + str(iterable*2))
    iterable += 2
    userInput = input("Enter stop to exit\n")
    if userInput == 'stop':
        False
        break