"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

Desired output:
Average spam confidence: 0.7507185185185187
"""

fileName = input("Please enter a file's name:\n")

try:
    file = open(fileName)
except:
    print("Coudn't open the file: " + fileName)
    quit()

lineCount = 0
totalConfidence = 0.0

for line in file:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lineCount += 1
    index = line.find('0')
    try:
        totalConfidence += float((line[index:]).strip())
    except:
        print("Error while parsing the string.")

print("Average spam confidence: " + str(totalConfidence / lineCount))
