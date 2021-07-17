import os

# path of this script
directory = os.getcwd()

print(directory)

# get fileName from user
filepath = directory + '/' + input("Enter filename: ")
  
# Creates a new file
#with open(filepath, 'w+') as fp:
#    pass


file = open(filepath, 'w+')

file.write("Hello, I am Kunal!")

file.seek(0)

print(file.read())

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com