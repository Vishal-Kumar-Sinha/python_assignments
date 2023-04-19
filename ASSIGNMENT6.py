"""1. You are given a sequence of number A 1 , A 2 ,…,A N . For each valid i,
the star value of the element A i  is the number of valid indices j&lt;i  such
that A j  is divisible by A i . Calculate the maximum star value of a given
sequence."""

def maxval(lst):
    star_list=[]
    for i in range(0,len(lst)):
        cnt=0
        for j in range(0,i):
            if(lst[j]%lst[i]==0):
                cnt+=1
        star_list.append(cnt)
    return star_list
lst=[]
lst=list(map(int,input("Enter list :: ").split()))
print("Star Value list :: ",maxval(lst))
print("Maximum star value of the above list :: ",max(maxval(lst)))

"""Output:
Enter list :: 6 1 4 3 1 2
Star Value list ::  [0, 1, 0, 1, 4, 2]
Maximum star value of the above list ::  4             """





"""2. A permutation p 1 ,p 2 ...p N  of {1,2,...,N} is beautiful if p i &amp;p
 i+1  is greater than 0 for every 1≤i&lt;N . You are given an integer N, and 
 your task is to construct a beautiful permutation of length N or determine 
 that it&#39;s impossible.
*a&amp;b denotes the  bitwise AND  of a and b.
Beautiful permutation of 3 and 5. If N=4 it is not possible
1 3 2
2 3 1 5 4          """

def permu_nms(nums):
    lst=[[]]
    for i in nums:
        templst=[]
        for j in lst:
            for k in range(len(j)+1):
                templst.append(j[:k]+[i]+j[k:])
                lst=templst
    return lst
def beauty_permu(num):
    lst=permu_nms(num)
    res=[]
    for i in range(0,len(lst)):
        flag=True
        for j in range(0,len(lst[i])-1):
            if((lst[i][j] & lst[i][j+1])==0):
                flag=False
                break
        if(flag==True):
            res.append(lst[i])
    return res
n=int(input("Enter max number :: "))
num=[]
for i in range(1,n+1):
    num.append(i)
lst=beauty_permu(num)
if(len(lst)==0):
    print("!!! Beautiful permutation is not possible !!!")
else:
    print("Beautiful permutation :: ",lst)

"""Output:
Enter max number :: 3
Beautiful permutation ::  [[2, 3, 1], [1, 3, 2]]   """