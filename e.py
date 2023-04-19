"""5. Write a Python program to print every integer between 1 and n divisible by m. Also report whether
the number that is divisible by m is even or odd."""


m=int(input("Enter m :: "))
n=int(input("Enter n :: "))
for i in range(1,n):
  if i%m==0:
    print(i,"is divisible by",m)
    if i%2==0:
      print(i,"is even.")
    else:
      print(i,"is odd.")
