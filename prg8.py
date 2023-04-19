n=int(input("Enter n :: "))
for i in range(n):
  t=65
  for j in range(i+1):
    print(chr(t),end=' ')
    t+=1
  print()
