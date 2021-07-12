"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

Desired Output
0.8475

"""

text = "X-DSPAM-Confidence:    0.8475"

index = text.find('0')

try:
    number = float(text[index:])
except:
    print("Error while parsing.")

print(number)

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com