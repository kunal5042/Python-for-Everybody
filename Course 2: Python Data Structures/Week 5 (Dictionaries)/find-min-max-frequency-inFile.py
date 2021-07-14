def create_Handle():
    name = input("Please enter a file name:\n")

    try:
        handle = open(name)
        print("File was found!\nOperating on the data.")
    except:
        print("File name: " + name + " can't be opened.")
        handle = None
    return name,handle

def createDictionary(handle):
    counts = dict()
    try:
        for line in handle:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
    except:
        print("Can't operate, because no data was provided.")
    return counts

def find_Max_and_Min(counts):
    mostFrequentWordCount = None
    mostFrequentWord = None
    leastFrequentWord = None
    leastFrequentWordCount = None

    leastFrequencyWordsDictionary = dict()
    maxFrequencyWordsDictionary = dict()

    for word, count in counts.items():
        if mostFrequentWordCount is None or count  >= mostFrequentWordCount:
            if mostFrequentWordCount == count:
                maxFrequencyWordsDictionary[word] = maxFrequencyWordsDictionary.get(word,count)
            
            mostFrequentWord = word
            mostFrequentWordCount = count

        if leastFrequentWord is None or leastFrequentWordCount >= count:
            if leastFrequentWordCount == count:
                leastFrequencyWordsDictionary[word] = leastFrequencyWordsDictionary.get(word,count)
        
            leastFrequentWord = word
            leastFrequentWordCount = count
        
        if word == "Kunal":
            print(word,count, leastFrequentWordCount)

    return mostFrequentWordCount,mostFrequentWord,leastFrequentWord,leastFrequentWordCount,leastFrequencyWordsDictionary, maxFrequencyWordsDictionary

       


def print_Format(name, mostFrequentWordCount, mostFrequentWord, leastFrequencyWord, leastFrequencyWordCount, leastFrequencyWordsDictionary, maxFrequencyWordsDictionary):
    print()
    print("In file " + name + "\n")
    print("Most frequent word:")
    print("The word \t'" + str(mostFrequentWord) + "'" + "\nFrequency \t'" + str(mostFrequentWordCount) + "'")

    print()
    print("Least frequent word:")
    print("The word \t'" + str(leastFrequencyWord) + "'" + "\nFrequency \t'" + str(leastFrequencyWordCount) + "'")

    if not leastFrequencyWordsDictionary:
        print()
    else:
        printDictionary(leastFrequencyWordsDictionary,"least")

    if not maxFrequencyWordsDictionary:
        print()
    else:
        printDictionary(maxFrequencyWordsDictionary,"most")



def printDictionary(dictionary,string):
    if string == "least":
        print("\nYou are seeing this message, because there exists more than one word whose frequency is eqaul to the frequency of the least frequent word.")
        count = 0
        flag = True

        for key in dictionary.items():
            count += 1

        if count > 1:
            while flag == True:
                choice = input("\nEnter 1 to print list of those words.\nEnter 2 to exit. Default: 2\n")
                try:
                    choice = int(choice)
                    if choice == 1:
                        for key, value in dictionary.items():
                            print("Frequency: " + str(value) + "\t" + key )
                    elif choice == 2:
                        flag = False
                except:
                    print("Invalid input!, Default 2")
                    flag = False
    elif string == "most":
        print("\nYou are seeing this message, because there exists more than one word whose frequency is eqaul to the frequency of the most frequent word.")        
        count = 0
        flag = True

        for key in dictionary.items():
            count += 1

        if count > 1:
            while flag == True:
                choice = input("\nEnter 1 to print list of those words.\nEnter 2 to exit. Default: 2\n")
                try:
                    choice = int(choice)
                    if choice == 1:
                        for key, value in dictionary.items():
                            print("Frequency: " + str(value) + "\t" + key )
                    elif choice == 2:
                        flag = False
                except:
                    print("Invalid input!, Default 2")
                    flag = False
 
        





name, handle = create_Handle()

counts = createDictionary(handle)

mostFrequentWordCount, mostFrequentWord, leastFrequentWord, leastFrequentWordCount, leastFrequencyWordsDictionary, maxFrequencyWordsDictionary = find_Max_and_Min(counts) 

print_Format(name, mostFrequentWordCount, mostFrequentWord, leastFrequentWord, leastFrequentWordCount, leastFrequencyWordsDictionary, maxFrequencyWordsDictionary)

        
# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com