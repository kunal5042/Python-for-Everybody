myDict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
tuple(myDict)

print(myDict)
print()

print(sorted(myDict))
print()

#List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.
print( sorted([ (value,key) for key,value in myDict.items()], reverse=True))
print()

print( sorted([ (value,key) for key,value in myDict.items()], reverse=False))
print()
