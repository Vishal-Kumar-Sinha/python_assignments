print("Enter numbers")
print("(Enter 'q' to stop)")
while True:
  n=input()
  if n=='q' or n=='Q':
    break
  n=int(n)
  t=n
  r=0
  while(t!=0):
    d=t%10
    r=r*10+d
    t=t//10
  if(n==r):
    print(n, "is a Palindrome Number")
  else :
    print(n, "is not a Palindrome Number")
