"""1. Today potatoes price are change day by day. Let a salesman will purchase 
it on some day and sell it on other day. Let us consider for a week price of 
potato are 100, 200, 300, 80, 30, 200, 250 meaning is that day1 price 100, day2
price is 200 and so on. You have found out on which day salesman will buy and
sell the potato so that for a week his profit is maximum.In the above case 
salesman will
buy on day1 and sell it on day3,
buy on day 5 and sell it on day 7.
(consider Number of days may be 2 to 30.) """
def max_profit(A):
    max_prices = []
    min_prices = []
    for i in range(1, len(A) - 1):
        if (A[i - 1] < A[i] and A[i] > A[i + 1]):
            if (len(min_prices) == 0):
                min_prices.append(A[0])
            max_prices.append(A[i])
        elif (A[i - 1] > A[i] and A[i] < A[i + 1]):
            min_prices.append(A[i])
        if (i == len(A) - 2 and A[i] < A[i + 1]):
            max_prices.append(A[i + 1])
        if (i == 1 and A[i - 1] < A[i]):
            min_prices.append(A[i - 1])
    if (len(A) == 2 and A[0] < A[1]):
        max_prices.append( A[1] )
        min_prices.append( A[0] )
    i = 1
    profit = 0
    for sp, cp in zip(max_prices, min_prices):
        print(f"{i}) S.P. - C.P. = {sp} - {cp} = {sp - cp}")
        profit += (sp - cp)
        i += 1
    return profit
prices = list(map(int, input("Enter the prices (seperated by space): ").split()))
print("Max Profit:", max_profit(prices))

"""Output:  
Enter the prices (seperated by space): 100 120 45 752 62
1) S.P. - C.P. = 120 - 100 = 20
2) S.P. - C.P. = 752 - 100 = 652
Max Profit: 672        """



"""2. Consider a string contains any characters of length. If two consecutive 
characters is same they are called 2- neighbour, if 3 consecutive characters 
are same they are called 3-neighbour and so on. You have to find out a neighbour
of maximum size in length."""
def mnb(S):
    x,c,num=S[0],0,0
    for i in S:
        if (i==x):
            c+=1
        else:
            num=max(num,c)
            c=1
        x=i
    return num
S=input("Enter the string :: ")
print("The maximum length of the neighbour is :: ",mnb(S))
"""Output:
Enter the string : aab
The maximum length of the neighbour is :  2   """



"""3.	Insert an element in all position of a list"""
lst=[]
n = int(input("Enter number of elements :: "))
for i in range(0,n):
	ele=int(input())
	lst.append(ele)
print("Original list :: ") 
print(lst)
x=int(input("Enter element to insert :: "))
for pos in range(1,n+2):
       m=lst[:pos-1]+[x]+lst[pos-1:]
       print(m)

"""Output:
Enter number of elements :: 5

1

22

63

98

7
Original list :: 
[1, 22, 63, 98, 7]

Enter element to insert :: 10
[10, 1, 22, 63, 98, 7]
[1, 10, 22, 63, 98, 7]
[1, 22, 10, 63, 98, 7]
[1, 22, 63, 10, 98, 7]
[1, 22, 63, 98, 10, 7]
[1, 22, 63, 98, 7, 10]                """