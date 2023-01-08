"""
Write a python script to check whether a given quadratic equation has two
real & distinct roots, real & equal roots or imaginary roots
"""

# taking corresponding values of the quadratic equation 
a, b, c = int(input("Enter corresponding values of quadratic equation 'a, b, c' : ")),
int(input()), int(input())

# to check roots of the quadratic equation first we have to calculate discriminant
# discriminant = b*b - 4*a*c
# roots of the quadratic euqation depends on the discriminant value

"""
    if discriminant > 0 :
        roots are real and distinct
    if discriminant < 0 :
        roots are imaginary 
    if discriminant == 0 :
        roots are real and equal
"""

# calculating discriminant value
discriminant = b*b - 4*a*c

# evaluating roots
if discriminant > 0 :
    print("Roots are real & distinct")
elif discriminant < 0 :
    print("Roots are imaginary")
else :
    print("Roots are rea and equal")
