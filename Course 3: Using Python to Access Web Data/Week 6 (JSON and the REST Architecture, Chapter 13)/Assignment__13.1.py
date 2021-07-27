import urllib.request, urllib.parse, urllib.error
import json

url = input("Please enter a URL\n")

try:
    data = urllib.request.urlopen(url)
    print()
except:
    print("\nCan not connect to the server!")
    print("Exiting...")
    quit()

try:
    parsedJSON = json.loads(data.read().decode())
except:
    print("\nBad JSON fomat!")
    print("Exiting...")
    quit()

#print(parsedJSON)

sum = 0
for dictionary in parsedJSON["comments"]:
    try:
        count = int(dictionary["count"])
        sum += count
    except:
        print("Coudn't parse integer from the string: " + str(dictionary["count"]))

print(sum)

# July 27, 2021 

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com
