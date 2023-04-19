n=int(input("Enter number of rows :: "))
for i in range(n):
  for k in range(i+1):
     print('*',end=' ')
  print()
for i in range(n-1):
  for k in range(n-1,i,-1):
     print('*',end=' ')
  print()
