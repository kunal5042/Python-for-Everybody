import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x = "7">
            <id>5042</id>
            <name>Kunal Wadhwa</name>
        </user>
        <user x = "8">
            <id>5555</id>
            <name>Raghav Ahuja</name>
        </user>
    </users>
</stuff>'''

try:
    #We pass the string data, to fromstring() method which takes the string data parse it and create a tree.
    tree = ET.fromstring(data)
    #print(tree)
    #print(tree.find('users/user/name').text)
except:
    print("Bad XML format!")
    quit()

#Find all of the user tags under users
#And return a list of them
list = tree.findall('users/user')
#print(list)

print("User count: ", len(list))

#Kinda for tag in the list of tags
for item in list:
    try:
        print('Name : ' + item.find('name').text)
        print('Id   : ' + item.find('id').text)

        #From the tag, find the x attribute
        print('Attr : ', item.get("x"))
        print()
    except:
        print("\nCan't find the given tag in the XML data.")

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com