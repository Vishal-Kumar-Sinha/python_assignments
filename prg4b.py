x=int(input("Enter the value of x :: "))
sum=0
m=1
for i in range(1,7):
  fact=1
  for j in range(1,i+1):
    fact*=j
  term=x**i/fact
  sum+=term*m
  m=m*-1
print("Sum = ",sum)
