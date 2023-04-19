n=int(input("Enter n :: "))
t=65
for i in range(n):
  for j in range(i+1):
    print(chr(t),end=' ')
  t+=1
  print()
