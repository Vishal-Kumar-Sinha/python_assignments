n=int(input("Enter number of rows :: "))
for i in range(1,n+1):
  x=1
  while(x<2*i):
    if(x==1 or x==2*i-1):
      print('*',end='')
    else :
      print(' ',end='')
    x+=1
  print()
for i in range(n-1,0,-1):
  x=1
  while(x<2*i):
    if(x==1 or x==2*i-1):
      print('*',end='')
    else :
      print(' ',end='')
    x+=1
  print()
  
  """write first five programs in lab copy"""
  
