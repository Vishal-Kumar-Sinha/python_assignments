n=2
d=9
m=1
sum=0
for i in range(7):
  t=n/d
  sum+=t*m
  n+=3
  d+=4
  m*=-1
print("Sum = ",sum)
