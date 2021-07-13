var = None

if var is None: # Checking if the variable is None
  print("None")
else:
  print("Not None")


if var == None: # Checking if the variable is None
  print("None")
else:
  print("Not None")

typeOfNone = type(None) 

print(typeOfNone)

# Comparing None with none and printing the result
print (None == None)

# Comparing none with False and printing the result
print(None == False)

# Declaring an empty string
str = ""
# Comparing None with empty string and printing the result
print (str == None)

"""
Output: 

None
None
<class 'NoneType'>
True
False
False

"""