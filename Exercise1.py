#I am going to use the Math library to calculate the hypotenuse of a right angled triangle
 
import math


a = float(input("What is the length of a: "))
b = float(input("What is the length of b: "))

c = math.sqrt(a**2 + b**2)

#same as c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"\nThe length of c (hypotenuse) is : {c}")

#This gives the hypotenuse of the triangle