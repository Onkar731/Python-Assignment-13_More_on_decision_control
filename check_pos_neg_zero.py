"""
Write a python script to check whether a given number is positive, negative or zero
"""

# taking input from the user
num = int(input("Enter a number : "))

# evaluating whether a given number is positive, negative or zero
if num > 0 :
    print(num, "is positive")
elif num < 0 :
    print(num, "is negative")
else :
    print("zero")