"""

Colon operator.

The second number is one beyond the end of the slice -
"up tp but not including"

If the second number is beyond the end of the string, it stops at the end.

"""

stringVar = "KUNAL WADHWA"

print(stringVar[0:5])
print(stringVar[6:11])
print(stringVar[0:2423])

print(stringVar[:3])
print(stringVar[:444])
print(stringVar[:])
"""
Output:

KUNAL
WADHW
KUNAL WADHWA
KUN
KUNAL WADHWA
KUNAL WADHWA

"""



       

    
       
