"""

9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

Desired Output
cwen@iupui.edu 5

"""
def getFileHandle():
    try:
        file = open("mbox-short.txt")
        return file
    except:
        print()
        print("Please follow this link -> https://www.py4e.com/code3/mbox-short.txt\nAnd download the data from there and save it as Sample-Data.txt in the same directory as this program.\nAs this program operates on that data, it won't work unless that data has been fed to it.")
        file = None
        return file

def createEmailDictionary():
    
    sendersEmail = dict()
    for line in getFileHandle():
        if not line.startswith("From"):
            continue
    
        if line.startswith("From"):
            if line.startswith("From:"):
                continue
            else:
                list = line.split()
                sendersEmail[list[1]] = sendersEmail.get((list[1].strip()), 0) + 1
    return sendersEmail

def extractPC_fromEmailDict():
    maxValue = None
    maxKey   = None
    for key, value in createEmailDictionary().items():
        if maxValue is None or maxValue < value:
            maxValue = value
            maxKey   = key
    return maxKey, maxValue


prolificCommiterKey, prolificCommiterValue = extractPC_fromEmailDict()
print(prolificCommiterKey + " " + str(prolificCommiterValue))

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com