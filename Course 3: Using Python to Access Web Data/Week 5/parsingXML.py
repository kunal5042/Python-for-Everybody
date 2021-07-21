# 'as' is used to create an alias of the imported package
import xml.etree.ElementTree as ET

#XML data
data = '''<person>
    <name>Kunal</name>
    <phone type="intl">77777 88888
    </phone>
    <email hide = "yes"/>
</person>'''

try:
    #We pass the string data, tfo fromstring() method which takes the string data parse it and create a tree.
    tree = ET.fromstring(data)
    #print(tree)
except:
    print("Bad XML format!")
    quit()

print('Name : ' + tree.find('name').text)
#print("Tree position: " + str(tree.find('name')))
print('Phone: ' +  tree.find('phone').text )
#print("Tree position: " + str(tree.find('phone')))
print('Attr : ' + tree.find('email').get('hide'))

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com