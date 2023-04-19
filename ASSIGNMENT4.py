"""1. Implement stack using Python """
stack = [10, 20, 30, 60, 2, 90]
print ("stack elements: ");
print (stack)
stack.append(40)
stack.append(50)
print ("Stack elements after push opration...");
print (stack)
print (stack.pop (), " is removed/popped...")
print (stack.pop (), " is removed/popped...")
print (stack.pop (), " is removed/popped...")
print ("Stack elements after pop operation...");
print (stack)

"""Output:
stack elements: 
[10, 20, 30, 60, 2, 90]
Stack elements after push opration...
[10, 20, 30, 60, 2, 90, 40, 50]
50  is removed/popped...
40  is removed/popped...
90  is removed/popped...
Stack elements after pop operation...
[10, 20, 30, 60, 2]                             """



"""2. Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing
a series of operations. In each operation, select a pair of adjacent letters
that match, and delete them. Delete as many characters as possible using this 
method and return the resulting string. If the final string is empty, return 
Empty String """
s=input("Enter any string :: ")
while 1:
    i=0
    flag=0
    while i<len(s)-1:
        if s[i] == s[i+1]:
            s=s[:i]+s[i+2:]
            flag=1
        else:    
            i+=1
    if flag==0:
        break
if len(s)>0:        
    print("Reduced string :: ",s)
else:
    print("Empty String")
    
"""Output:
Enter any string :: aaabccddd
Reduced string ::  abd              """



"""3. Represent an integer number in Roman """
def prntRmn(n):
    num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    rom=["I","IV","V","IX","X","XL""L","XC","C","CD","D","CM","M"]
    i=12
    while n:
        q=n//num[i]
        n%=num[i]
        while q:
            print(rom[i],end="")
            q-=1
        i-=1 
x=int(input("Enter any integer number :: "))
print("Roman representation  is :: ",end="")
prntRmn(x)

"""Output:
Enter any integer number :: 32
Roman representation  is :: XXXII          """



"""4. Find the Twins primes between a range( Twin primes are pairs of prime 
numbers that have just one number between them: 5 and 7, 11 and 13, and 29 
and 31) """
def pri(n):
   for i in range(2,n):
      if n%i==0:
         return False
   return True
def t_pri(x,y):
   for i in range(x,y):
      j=i+2
      if(pri(i) and pri(j)):
         print("{:d} and {:d}".format(i,j))
a=int(input("Starting point :: "))
b=int(input("Ending point :: "))
print("\nTwin-prime numbers in the given range are :: ")
t_pri(a,b)

"""Output:
Starting point :: 10

Ending point :: 20

Twin-prime numbers in the given range are :: 
11 and 13
17 and 19         """



"""5. """
a=int(input("Starting point :: "))
b=int(input("Ending point :: "))
print("\nPalindromic prime numbers in the above range :: ")
for i in range(a,b):
        y = True
        if(str(i)==str(i)[::-1]):
            if(i>2):
                for a in range(2,i):
                    if(i%a==0):
                        y = False
                        break
                if y:
                    print(i,end=" ")
"""Output:
Starting point :: 100

Ending point :: 200

Palindromic prime numbers in the above range :: 
101 131 151 181 191     """