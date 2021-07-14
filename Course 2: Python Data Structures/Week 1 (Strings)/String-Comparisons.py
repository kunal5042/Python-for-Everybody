stringVar1 = "190905042"
stringVar2 = "5042"
stringVar3 = "Kunal"
stringVar4 = "Wadhwa"
stringVar5 = "abc"

def WeightOfString(stringVar):
    total = 0
    for character in stringVar:
        total += int(ord(character))
    return total

def WeightOfArrayOfStrings(stringArrayVar):
    count = -1
    for string in stringArrayVar:
        count += 1
        print("Index: " + str(count)  + "\tString : " + string + "\t\tWeight \t: " + str(WeightOfString(string)))


def MaximumAndMinimum_Value_Of_Strings(stringVar):
    String_With_Minimum_Value = None
    String_With_Maximum_Value = None
    for string in stringVar:
        if String_With_Minimum_Value is None:
            String_With_Minimum_Value = string
        
        if String_With_Maximum_Value is None:
            String_With_Maximum_Value = string
        
        if String_With_Minimum_Value > string:
            String_With_Minimum_Value = string
        
        if String_With_Maximum_Value < string:
            String_With_Maximum_Value = string

    print("Maximum            : " + String_With_Maximum_Value + "\t\tWeight \t: " + (str(WeightOfString(String_With_Maximum_Value))))
    print("Minimum            : " + String_With_Minimum_Value + "\t\tWeight \t: " + (str(WeightOfString(String_With_Minimum_Value))))
    print()


stringVar = ["Kunal", "Tanya", "Olivia", "5042", "123"]
WeightOfArrayOfStrings(stringVar)
MaximumAndMinimum_Value_Of_Strings(stringVar)


stringVar = ["AAA", "BBB", "CCC", "DDD"]
WeightOfArrayOfStrings(stringVar)
MaximumAndMinimum_Value_Of_Strings(stringVar)


stringVar = ["1234", "5678", "91011", "12131"]
WeightOfArrayOfStrings(stringVar)
MaximumAndMinimum_Value_Of_Strings(stringVar)

MaximumAndMinimum_Value_Of_Strings(stringVar1)
MaximumAndMinimum_Value_Of_Strings(stringVar2)
MaximumAndMinimum_Value_Of_Strings(stringVar3)

WeightOfArrayOfStrings(stringVar4)
MaximumAndMinimum_Value_Of_Strings(stringVar4)

MaximumAndMinimum_Value_Of_Strings(stringVar5)

"""
Output:
Index: 0	String : Kunal		Weight 	: 507
Index: 1	String : Tanya		Weight 	: 509
Index: 2	String : Olivia		Weight 	: 612
Index: 3	String : 5042		Weight 	: 203
Index: 4	String  : 123		Weight 	: 150
Maximum            : Tanya		Weight 	: 509
Minimum            : 123		Weight 	: 150

Index: 0	String : AAA		Weight 	: 195
Index: 1	String : BBB		Weight 	: 198
Index: 2	String : CCC		Weight 	: 201
Index: 3	String : DDD		Weight 	: 204
Maximum            : DDD		Weight 	: 204
Minimum            : AAA		Weight 	: 195

Index: 0	String : 1234		Weight 	: 202
Index: 1	String : 5678		Weight 	: 218
Index: 2	String : 91011		Weight 	: 252
Index: 3	String : 12131		Weight 	: 248
Maximum            : 91011		Weight 	: 252
Minimum            : 12131		Weight 	: 248

Maximum            : 9		Weight 	: 57
Minimum            : 0		Weight 	: 48

Maximum            : 5		Weight 	: 53
Minimum            : 0		Weight 	: 48

Maximum            : u		Weight 	: 117
Minimum            : K		Weight 	: 75

Index: 0	String : W		Weight 	: 87
Index: 1	String : a		Weight 	: 97
Index: 2	String : d		Weight 	: 100
Index: 3	String : h		Weight 	: 104
Index: 4	String : w		Weight 	: 119
Index: 5	String : a		Weight 	: 97
Maximum            : w		Weight 	: 119
Minimum            : W		Weight 	: 87

Maximum            : c		Weight 	: 99
Minimum            : a		Weight 	: 97
"""