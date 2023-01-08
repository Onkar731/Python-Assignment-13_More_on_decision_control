"""
Write a python script to check whether a given number is a three digit number or not
"""

# taking from the user
num = int(input("Enter a three digit number : "))

# checking whether a given number is a three digit number or not
# without using loop
if (num >= 100 and num <= 999) or (num <= -100 and num >= -999) :
    print(num, "is a three digit number")
else :
    print(num, "is not a three digit number")