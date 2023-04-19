"""6. Write a short program to check whether the square root of a number is prime or not."""
import math
a=int(input("Enter number :: "))
b=math.sqrt(a)
k=0
for i in range (2,b//2+1):
  if b%i==0:
    k=k+1
if k==0:
  print(b,"square root is prime")
else:
  print(b,"square root is not prime")
