try:
    handle = open('kunal.txt', 'r')
except:
    print("File not found!")

print(handle)
print()
print("Using file.read() function.")
print(handle.read())
print()

print("Using for loop.")
for line in handle:
    print(line.rstrip())

#New line \n is one character not two