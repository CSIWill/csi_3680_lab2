# William Eng
# weng2@oakland.edu
# Sort Numbered List

# Test Condition "1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97"

import bisect

myString = "1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97"

print("Original String is:\n{}".format(myString))

newNumber = input("Insert a number: ")
if newNumber.isdecimal() == True:
    # convert string of numbers to list of integers for bisect to work
    myList=myString.split(', ')
    for i in range(len(myList)):
        myList[i]= int(myList[i])
    bisect.insort(myList,int(newNumber))
    # convert back to string
    for i in range(len(myList)):
        myList[i]=str(myList[i])
    myString=', '.join(myList)
    print("Updated String is:\n{}".format(myString))
else:
    print("A valid input should contain only non-negative numbers")
    

    

