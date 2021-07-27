import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1305293.xml'
print("URL: " + url)

choice = input("\nEnter 1 to change the url\nEnter 2 to continue\n")
try:
    if int(choice) == 1:
        url = input("Enter the new url:\n")
    elif int(choice) != 2:
        print("Invalid choice: " + str(choice))
        print("Continuing with the default url: " + str(url))
except:
    print("\nInvalid input: " + str(choice))
    print("Continuing with the default url: " + str(url))
    print()

#XML = None
try:
    XML = urllib.request.urlopen(url, context=ctx).read()
    #print(XML)
    #for character in XML.decode():
        #print(character)
except:
    print("Can't connect to the host:\n" + url)

#list = None
try:
    XML_Tree = ET.fromstring(XML)
    lst = XML_Tree.findall('comments/comment')
    #print(list)
except:
    print("Bad XML format!")

count = 1
sum = 0
for item in lst:
    try:
        print("Node: " + str(count) + "\nSum: " + str(sum) + " + " + str(item.find('count').text) + "\t= " + str(sum + int(item.find('count').text)))
        print()

        sum += int(item.find('count').text)
        count += 1
        #print(item.find('count').text)
        #print()
    except:
        continue
    
print("Number of nodes\t: " + str(count))
print("Total sum\t: " + str(sum))

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com