"""1. Write a Python function to find the Max of three numbers """
a=int(input("Enter First number :: "))
b=int(input("Enter Second number :: "))
c=int(input("Enter Third number :: "))
def max_num(a,b,c):
    if(a>=b)and(a>=c):
        largest=a
    elif(b>=a)and(b>=c):
        largest=b
    else:
        largest=c
    return largest
print("Largest Number :: ",max_num(a,b,c))

"""Output:
Enter First number :: 12

Enter Second number :: 35

Enter Third number :: 5
Largest Number ::  35      """



"""2. Write a Python function to sum all the numbers in a list """
def sum_num(n):
    s=0
    for i in n:
        s+=i
    return s
print("Enter list elements :: ")
a=list(map(int,input().split()))
print("Sum of all elements :: ",sum_num(a))

"""Output:
Enter list elements :: 

5 78 54 3 -89
Sum of all elements ::  51  """



"""3. Write a Python function to multiply all the numbers in a list """
def mult_list(x):
    r=1
    for i in x:
         r=r*i
    return r
print("Enter list elements :: ")
n=list(map(int,input().split()))
print("Multiplication of all the numbers :: ",mult_list(n))

"""Output:
Enter list elements :: 

12 3 5 -2 9 -8
Multiplication of all the numbers ::  25920    """



"""4. Write a Python function to calculate the factorial of a number (a non-
negative integer). The function accepts the number as an argument. """
def fact_n(n):
    if n==0:
        return 1
    else:
        return n*fact_n(n-1)
n=int(input("Input an integer number :: "))
if n<0:
    print("...INVALID INPUT...")
else:
    print("Factorial is :: ",fact_n(n))

"""Output:
Input an integer number :: 5
Factorial is ::  120    """



"""5. Write a Python function that accepts a string and calculate the number 
of upper case letters and lower case letters """
def func(s):
    d={"U_C": 0,"L_C": 0}
    for c in s:
        if(c>='A' and c<='Z'):
            d["U_C"]+=1
        elif(c>='a' and c<='z'):
            d["L_C"]+=1
    print("No. of Upper case characters :: ",d["U_C"])
    print("No. of Lower case Characters :: ",d["L_C"])
str=input("Enter string :: ")
func(str)

"""Output:
Enter string :: The quick Brown Fox
No. of Upper case characters ::  3
No. of Lower case Characters ::  13     """



"""6. Write a Python function that takes a list and returns a new list with
unique elements of the first list"""
def u_list(x):
  n=[]
  for a in x:
    if a not in n:
      n.append(a)
  return n
print("Enter list elements :: ")
lst=list(map(int,input().split()))
print("List with unique elements :: ")
print(u_list(lst)) 

"""Output:
    Enter list elements :: 

1 1 2 2 5 5 9 1 8 8 6 5
List with unique elements :: 
[1, 2, 5, 9, 8, 6]   """



"""7. Write a Python function to check whether a number is perfect or not """
def per_num(n):
    s=0
    for x in range(1,n):
        if n%x==0:
            s+=x
    return s==n
a=int(input("Enter any integer number :: "))
if a>0 and per_num(a)==True:
    print("It is a perfect number.")
elif a>0 and per_num(a)==False:
    print("It is not a perfect number.")
else:
    print("...INVALID INPUT...")

"""Output:
Enter any integer number :: 6
It is a perfect number.             """



"""8. Write a Python function that checks whether a passed string is
palindrome or not """
def Pal_num(st):
	l_p=0
	r_p=len(st)-1
	while r_p>=l_p:
		if not st[l_p]==st[r_p]:
			return False
		l_p+=1
		r_p-=1
	return True
s=input("Enter string :: ")
if Pal_num(s)==True:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")

"""Output:
Enter string :: malayalam
The string is palindrome.    """



"""9. Write a Python function to check whether a string is a pangram or not"""
def pang_str(str):
   alphabet="abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True
s=input("Enter string :: ")
if pang_str(s)==True:
   print("The string is pangram.")
else:
   print("The string is not pangram.")
   
"""Output:
Enter string :: The quick brown fox jumps over the lazy dog
The string is pangram.     """


"""10. Write a Python program that accepts hyphen-separated sequence of words
as input and prints the words in a hyphen-separated sequence after sorting 
them alphabetically """
items=[n for n in input("Enter hyphen-separated sequence of words :: ").split('-')]
items.sort()
print("Sorted sequence :: ",end='')
print('-'.join(items))

"""Output:
Enter hyphen-separated sequence of words :: green-red-yellow-black-white-pink
Sorted sequence :: black-green-pink-red-white-yellow     """



"""11. Write a python program to show the permutation and combination of a 
inputted List """
def toString(List):
	return "-".join(List)
def npr(a,l,r):
	if l==r:
		print(toString(a),end="  ,  ")
	else:
		for i in range(l,r+1):
			a[l],a[i]=a[i],a[l]
			npr(a,l+1,r)
			a[l],a[i]=a[i],a[l]
def ncr(lst,n):
 if n==0:
  return [[]]
 l=[]
 for i in range(0,len(lst)):
  m=lst[i]
  ans=lst[(i+1):]
  for p in ncr(ans,n-1):
   l.append([m]+p)
 return l
string=input("Enter any string :: ")
num=int(input("Enter number for combinations :: "))
n=len(string)
a=list(string)
print("\nPermutations :: \n")
npr(a,0,n-1)
print("\n\nCombinations :: \n")
print(ncr([x for x in string],num))

"""Output:
Enter any string :: atm

Enter number for combinations :: 2

Permutations :: 

a-t-m  ,  a-m-t  ,  t-a-m  ,  t-m-a  ,  m-t-a  ,  m-a-t  ,  

Combinations :: 

[['a', 't'], ['a', 'm'], ['t', 'm']]          """