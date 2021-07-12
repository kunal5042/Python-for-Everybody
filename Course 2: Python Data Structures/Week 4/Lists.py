"""

List constants:
List constans are surrounded by square brackets and the elements in the list are spearated by commas.

A list element can be any Python object - even another list.

A list can by empty.

Lists Are Mutable:

Strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any change.

Lists are "mutable" - we can change an element of alist using the index operator.

"""

#Example of list constant
tv_Shows1 = [ "FRIENDS", "Money Heist", "The Year Earth Changed"]

#lenght of list constant
print(len(tv_Shows1))

#range of list constant
print(range(len(tv_Shows1)))

#element at position index 0
print(tv_Shows1[0])
print()

#Iterating throught all elements of list constant
for series in tv_Shows1:
    print(series)

tv_Shows2 = [ "The Morning Show", "SEE", "Finding Jacob", "Kunal's Late Night Show"]
#Another approach to interation
print()
for index in range(len(tv_Shows2)):
    print(tv_Shows2[index])

#Concatenating two lists:
all_Shows = tv_Shows1 + tv_Shows2

#Slicing in lists
print()
print(all_Shows[2:5])

#Append function
print()
all_Shows.append("How I Met Your Mother")
print(all_Shows[len(all_Shows) - 1])

all_Shows.append("Breaking Bad")

#in operator in lists
print()
print("SEE" in all_Shows)

#not in operator in lists
print("NULL" not in all_Shows)

#sort function in Lists
print()
print("All shows in sorted order:")
all_Shows.sort()
print(all_Shows)

#insert function in List
print()
print("Inserted a new show at the front of the list 1:")
tv_Shows1.insert(0,"Abracadabra!")
print(tv_Shows1)

#max and min functions in lists
print()
print("Alphabetically minimum:")
print(min(all_Shows))
print()
print("Alphabetically maximum:")
print(max(all_Shows))

#sum function in Lists
list3 = [1,2,3,4,5]
print()
print("Sum of list 3")
print(str(sum(list3)))
#sum function can't be used on list of strings

list4 = [2.2, 3.3, 4.4, 5.5]
print()
print("Sum of list 4:")
print(sum(list4))
print("Average of list 4:")
print((sum(list4)/len(list4)))

#Best Friends: Strings and Lists
print()

#*******************************#
#split function in Strings
stringVar1 = "This will be converted into a list with each spaced word as a different element of the list of strings. Using split function."

list5 = stringVar1.split()

print("List 5:")
print(list5)


stringVar2 = "Now,the,syntax,of,the,string,is,different,and,split(),basically,looks,for,spaces,which,are,not,present,here.,\n,So,what,we,can,do,here,is,to,pass,a,delimiter,character,to,the,split,function."
#as follows:
list6 = stringVar2.split(",")
print()
print(list6)

print("Another example of split delimiter.")

stringVar3 = "We; are; changing; the; syntax; again."
print()
list7 = stringVar3.split(";")
print(list7)
print()

#*********************************************#
#Double split pattern
someData = "From kunalwadhwa.cs@gmail.com Mon Jul 12 01:11:11 2021"

listOfsomeData = someData.split()
email = listOfsomeData[1]
print("Email:")
print(email)
print()
piecesOfEmail = email.split("@")
print()
print("Sender's address and email provider:")
print(piecesOfEmail)


"""
LIST SUMMARY:
Concept of a collection
Lists and definite loops
Indexing and lookup
List multability
Functions: len, min, max, sum
Slicing lists
List methods: append, remove
Sorting lists
Splitting strings into lists of worlds
Using split to parse strings

"""

"""
OUTPUT:
3
range(0, 3)
FRIENDS

FRIENDS
Money Heist
The Year Earth Changed

The Morning Show
SEE
Finding Jacob
Kunal's Late Night Show

['The Year Earth Changed', 'The Morning Show', 'SEE']

How I Met Your Mother

True
True

All shows in sorted order:
['Breaking Bad', 'FRIENDS', 'Finding Jacob', 'How I Met Your Mother', "Kunal's Late Night Show", 'Money Heist', 'SEE', 'The Morning Show', 'The Year Earth Changed']

Inserted a new show at the front of the list 1:
['Abracadabra!', 'FRIENDS', 'Money Heist', 'The Year Earth Changed']

Alphabetically minimum:
Breaking Bad

Alphabetically maximum:
The Year Earth Changed

Sum of list 3
15

Sum of list 4:
15.4
Average of list 4:
3.85

List 5:
['This', 'will', 'be', 'converted', 'into', 'a', 'list', 'with', 'each', 'spaced', 'word', 'as', 'a', 'different', 'element', 'of', 'the', 'list', 'of', 'strings.', 'Using', 'split', 'function.']

['Now', 'the', 'syntax', 'of', 'the', 'string', 'is', 'different', 'and', 'split()', 'basically', 'looks', 'for', 'spaces', 'which', 'are', 'not', 'present', 'here.', '\n', 'So', 'what', 'we', 'can', 'do', 'here', 'is', 'to', 'pass', 'a', 'delimiter', 'character', 'to', 'the', 'split', 'function.']
Another example of split delimiter.

['We', ' are', ' changing', ' the', ' syntax', ' again.']

Email:
kunalwadhwa.cs@gmail.com


Sender's address and email provider:
['kunalwadhwa.cs', 'gmail.com']

"""