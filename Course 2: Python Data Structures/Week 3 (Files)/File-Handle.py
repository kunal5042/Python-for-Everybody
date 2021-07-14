"""
A file handle open for read can be treated as a sequence of strings where each line in the files is a string in the sequence.

We can use the for statement to iterate through a sequence.

Remember - a sequence is an ordered set."""

count = 0
NumberOfLines = None
choice = 0
flag = True
print("Example of keys: Timothy, John, gmail.com, yahoo.com\nEt cetera!")
while flag:
    print("\nEnter 1 to search for a key in us-Sample-data.csv\nEnter 2 to exit\n")
    choice = input()
    if choice == '1':
        key = input("Please enter a key!\n")
        file = open('us-Sample-data.csv')
        keyFrequency = 0
        for line in file:
            count += 1
            index = line.find(key)
            if index != -1:
                keyFrequency += 1
                print()
                print(str(keyFrequency) + " :")
                print("Found " + key + " in line number: " + str(count) + " at index " + str(index))
                print(line)
        if NumberOfLines is None:
            NumberOfLines = count
        print("Found " + key + " " + str(keyFrequency) + " times in the file.")
        count = 0
    if choice == '2':
        flag = False


print("\nTotal number of files in us-Sample-data.csv\t: ", NumberOfLines)
print()

