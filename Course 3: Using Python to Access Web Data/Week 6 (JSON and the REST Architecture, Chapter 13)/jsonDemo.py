import json
data = """{
    "name" : "Kunal",
    "phone": "8888877777",
    "email": {
        "hide": "yes"
        }
    }"""

#Returns a python dictionary
info = json.loads(data)
print()
print(info)

print()
print("Name:" , info["name"])
#info is a dictionary object and email inside it is also a python dictionary, that's why we use [][]to access key inside a python dictionary inside another python dictionary
print("Hide:" , info["email"]["hide"])

#JSON represents data as nested "lists" and "dictionaries"

# July 27, 2021 

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com
