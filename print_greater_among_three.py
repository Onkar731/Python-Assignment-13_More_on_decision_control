"""
Write a python script to print greater among three numbers.
Print number only once even if the numbers are the same.
"""

# taking three numbers from the user
num1, num2, num3 = int(input("Enter three numbers : ")), int(input()), int(input())

# finding for greater among three
if num1 > num2 and num1 > num3 :
    print(num1, "is GREATER")
elif num2 > num3 :
    print(num2, "is GREATER")
else :
    if num1 == num2 == num3 :
        print("All are equals", num1)
    else :
        print(num3, "is GREATER")