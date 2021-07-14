"""
TUPLES:

Lists like indexing, are immutable.
Any methods or functions in the list which change the data in the lists can't be used with tuples.

TUPLES ARE MORE EFFICIENT:

Since python does not have to build tuple structures to be modifiable, they are simpler more efficient in terms of memory use and performance than lists.

So in our program when we are making "temporary variables" we prefer tuples over lists.

"""

#TUPLES AND DICTIONARIES:
#THE items() method in dictionaries returns a list of (key, value) tuples.
#The returned list is comprised of two tuples, i.e key and value.

#TUPLES ARE COMPARABLE:
#The comparison operators work with tuples and other sequences. If the first item is equal, python goes on to the next element, and so on, until it finds elements that differ.

"""
SORTING LISTS OF TUPLES:
We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary.

First we sort the dictionary by the key using the items() method and sorted() function

We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence.

If we could construct a list of tuples of the form (value, key) we could sort by value.

We do this with a for loop that creates a list of tuples.
"""

myDict = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}

someList = list()
for key, value in myDict.items():
    someList.append((value, key))

print(someList)

someList = sorted(someList, reverse=True)
print(someList)

#Another way to sort in reverse.
someList.sort(reverse=False)
print(someList)

"""
TUPLES SUMMARY:
Tuple syntax
Immutability
Comparability
Sorting

Tuples in assignment statements.
Sorting dicitionaries by either key or value."""