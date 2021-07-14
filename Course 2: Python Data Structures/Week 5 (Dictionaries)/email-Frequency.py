def SampleDataHandle():
    #Open the file mbox-short.txt
    try:
        file = open("Sample-Data.txt")
    except:
        print()
        print("Please follow this link -> https://www.py4e.com/code3/mbox-short.txt\nAnd download the data from there and save it as Sample-Data.txt in the same directory as this program.\nAs this program operates on that data, it won't work unless that data has been fed to it.")
        file = None
    return file

def extractEmails_inDictionary():
    Count = 0
    emails = dict()

#Reading the file line by line
    try:
        for line in file:
        #Finding lines that starts with "From"
            if not line.startswith("From"):
                continue

        #Making sure to not include the lines that start with "From:"
            if line.startswith("From:"):
                continue
        
            else:
            #Parsing the lines that starts with "From"
                list = line.split()

            #Non if approach for the same
                emails[list[1]] = emails.get(list[1],0) + 1

            #if-else approach for the same
            #if list[1] in emails:
            #    emails[list[1]] = emails[list[1]] + 1
            #else:
            #    emails[list[1]] = 1
    except:
        print("")
    return emails



file = SampleDataHandle()
emails = extractEmails_inDictionary()


def printEmails_withFrequency():
    for key in emails:
        print("Frequency: " + str(emails[key]) + "\t" + key )

printEmails_withFrequency()

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com