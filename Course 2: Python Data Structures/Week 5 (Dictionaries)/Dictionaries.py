"""

Dictionaries:

Dic are python's most powerful data collection.
Dic allow us to do fast database-like operations in python.
Dic have different names in different languages.
For example:
Associative Arrays - Perl / PHP
Properties or Map or HashMap - Java
Property Bag - C# /.Net

"""

def dictionaryDemo():
    #Initialization
    myDictionary = dict()

#Dictionaries are like bags - no order
    myDictionary["Kunal5042"]   = 1

#So we index the things we put in the dictionary with a "lookup tag"
    myDictionary["Tanya"]       = 7
    myDictionary["Macbook Pro"] = 2399.99

#To get something out we use the exact same label
    print("Macbook Pro: $" + str(myDictionary["Macbook Pro"]))

#An object whose internal state can be changed is mutable. On the other hand, immutable doesn't allow any change in the object once it has been created

#Dictionary contents are mutable
    myDictionary["Kunal5042"] = myDictionary["Kunal5042"] + 5041
    print("kunal" + str(myDictionary["Kunal5042"]))

#Dictionaires are like lists except that they use keys instead of numbers to look up values.

#Changing values of the keys
    myDictionary["Tanya"] = 9000
    print("Power level over " + str(myDictionary["Tanya"]) + "!")

dictionaryDemo()


# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com