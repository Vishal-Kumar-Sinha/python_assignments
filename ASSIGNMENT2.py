"""1.Write a Python Program to Find the Smallest Divisor of an Integer other
than 1."""
n=int(input("Enter an integer :: "))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is :: ",a[0])
"""Output :
Enter an integer :: 45
Smallest divisor is ::  3       """

"""2.Write a Python Program to Check whether a Number is a Palindrome or
not."""
n=int(input("Enter any number :: "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome.")
else:
    print("The number isn't a palindrome.")
"""Output :
Enter any number :: 11
The number is a palindrome.   """

"""3.Write a Python Program to print the Prime Factors of an Integer.
"""
n=int(input("Enter an integer :: "))
print("Prime Factors are :: ")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1
"""Output :
Enter an integer :: 45
Prime Factors are :: 
3
5        """

"""4.Print the following pattern
1
2 1
4 2 1
8 4 2 1   """
n=int(input("Enter number of rows :: "))
for i in range(n):
    p=i
    for j in range(i+1):
        print(2**p,end=' ')
        p=p-1
    print()
"""Output :   
Enter number of rows and columns :: 8
1 
2 1 
4 2 1 
8 4 2 1 
16 8 4 2 1 
32 16 8 4 2 1 
64 32 16 8 4 2 1 
128 64 32 16 8 4 2 1      """

"""5.Print the following Pattern
* * * * 
*     * 
*     * 
* * * *   """
n=int(input("Enter any Side of a Square  :: "))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
"""Output :   
Enter any Side of a Square  :: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * *       """

"""6.The set of input is given as ages. Then print the status according to the rules
Age Status
1-1 in born
2-10 child
11-17 young
18-49 adult
50-79 old
&gt;80 very old              """
n=int(input("Enter age in years :: "))
if(n==1):
    print("in born")
elif(n>=2 and n<=10):
    print("child")
elif(n>=11 and n<=17):
    print("young")
elif(n>=18 and n<=49):
    print("adult")
elif(n>=50 and n<=79):
    print("old")
elif(n>=80):
    print('very old')
else:
    print("...invalid input...")
"""Output :  
Enter age in years :: 56
old            """

"""7.Convert a decimal number to a number of a given base b.
"""
n=int(input("Enter decimal number (base 10) :: "))
b=int(input("Enter base for conversion :: "))
x,i=0,0
while(n!=0):
    r=n%b
    x=((10**i)*r)+x
    i=i+1
    n=n//b
print("Converted number :: ")
print(x)
"""Output :
Enter decimal number (base 10) :: 12

Enter base for conversion :: 2
Converted number :: 
1100            """
