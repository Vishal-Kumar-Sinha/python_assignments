"""3. Write a program to input 3 sides of a triangle and print whether it is an equilateral, scalene or
isosceles triangle."""


a=float(input("Enter first side of the triangle :: "))
b=float(input("Enter second side of the triangle :: "))
c=float(input("Enter third side of the triangle :: "))
if a==b and b==c:
  print("Equilateral triangle")
elif((a==b and b!=c) or (b==c and a!=b) or (c==a and a!=b)):
  print("Isosceles triangle")
else:
  print("Scelene triangle")
