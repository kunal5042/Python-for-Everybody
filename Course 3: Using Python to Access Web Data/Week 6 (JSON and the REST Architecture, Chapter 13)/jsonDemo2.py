import json

data = """
[
    {
        "id": "5042",
        "name": "Kunal",
        "age": "20"
    } ,
    {
        "id": "2405",
        "name": "Tanya",
        "age": "20"
    }
]"""

# This time it returns a list of dicitionaries, because the data is enclosed in square brackets.
info = json.loads(data)
print()
print(info)
print()


# July 27, 2021 

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com
