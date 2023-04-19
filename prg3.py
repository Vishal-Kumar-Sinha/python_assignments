n=int(input("Enter the value of n :: "))
sum=0
for i in range(n+1):
  fact=1
  for j in range(1,i):
    fact*=j
  term=1/fact
  sum+=term
print("Sum =",sum)
