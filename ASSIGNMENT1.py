#1.
#Given a string of length greater than 2, return a string except 1st and last characters
str="vishalkumarsinha"
x=len(str)
strng=str[1:x-1]
print(strng)
#output:   ishalkumarsinh

#2.
#Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string
s1="vishalkrsinha"
s2="3cse3"
x=s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
print(x)
#output:   v3ksa3

#3.
#Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
s1="potter"
s2="gold"
x=s1[:len(s1)//2]+s2+s1[len(s1)//2:]
print(x)
#output:   potgoldter

#4.
#Find all occurrences of “India” in given string ignoring the case
str1="I live in India. INDIA is a great country and I love my India."
str2=str1.lower()
x=str2.count("india")
print(x)
#output:   3

#5.
#Find the last position of a substring “Emma” in a given string
str1="Emma is a good girl. Saheli lives with Emma and her sister."
x=str1.rfind("Emma")
print(x)
#output:   39

#6.
#Display the two substring separated by space.
str1="abcdefg"
x=(str1[:len(str1)//2]+" "+str1[len(str1)//2:])
print(x)
#Output: abc defg

#7.
#Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list.
sampleList=[34,54,267,829,191,43,4]
print("Original list :: ",sampleList)
element=sampleList.pop(4)
print("List After removing element at index 4 :: ",sampleList)
sampleList.insert(2,element)
print("List after Adding element at index 2 :: ",sampleList)
sampleList.append(element)
print("List after Adding element at last :: ",sampleList)
#Output:
"""
Original list ::  [34, 54, 267, 829, 191, 43, 4]
List After removing element at index 4 ::  [34, 54, 267, 829, 43, 4]
List after Adding element at index 2 ::  [34, 54, 191, 267, 829, 43, 4]
List after Adding element at last ::  [34, 54, 191, 267, 829, 43, 4, 191]      """

#8.
#Reverse the following tuple aTuple = (10, 20, 30, 40, 50)
aTuple = (10, 20, 30, 40, 50)
print(aTuple[::-1])
#Output: (50, 40, 30, 20, 10)

#9.
#Access value 20 from the following tuple aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])
#Output: 20

#10.
#Unpack the following tuple into 4 variables aTuple = (10, 20, 30, 40)
aTuple = (10, 20, 30, 40)
a,b,c,d=aTuple
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
#Output:
"""
a= 10
b= 20
c= 30
d= 40        """

#11.
#Swap the following two tuples tuple1 = (11, 22) tuple2 = (99, 88)
tuple1 = (11, 22) 
tuple2 = (99, 88)
print("Before swapping :: ",tuple1,tuple2)
tuple1,tuple2=tuple2,tuple1
print("After swapping :: ",tuple1,tuple2)
#Output:
"""
Before swapping ::  (11, 22) (99, 88)
After swapping ::  (99, 88) (11, 22)   """

#12.
#Copy element 44 and 55 from the following tuple into a new tuple tuple1 = (11, 22, 33, 44, 55, 66)
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[3:-1]
print(tuple2)
#Output: (44, 55)

#13.
#Modify the first item (22) of a list inside a following tuple to 222 tuple1 = (11, [22, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)
#Output: (11, [222, 33], 44, 55)

#14.
#Below are the two lists convert it into the dictionary keys = ['Ten', 'Twenty', 'Thirty'] values = [10, 20, 30]
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
sampleDict=dict(zip(keys,values))
print(sampleDict)
#Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

#15.
#Merge following two Python dictionaries into one dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)
#Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#16.
#Check if a value 200 exists in a dictionary sampleDict = {'a': 100, 'b': 200, 'c': 300}
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict.values())
#Output: True

#17.
#Rename key city to location in the following dictionary sampleDict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
sampleDict = { "name": "Kelly",  "age":25,  "salary": 8000,  "city": "New york"}
sampleDict['location']=sampleDict.pop('city')
print(sampleDict)
#Output: {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

#18.
#Get the key corresponding to the minimum value from the following dictionary sampleDict = { 'Physics': 82, 'Math': 65, 'history': 75}
sampleDict = {'Physics': 82, 'Math': 65, 'history': 75}
print(min(sampleDict, key=sampleDict.get))
#Output: Math

#19.
#Given a Python dictionary, Change Brad’s salary to 8500 sampleDict = { 'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 6500}}
sampleDict = { 'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},  'emp3': {'name': 'Brad', 'salary': 6500}}
sampleDict['emp3']['salary'] = 8500
print(sampleDict)
#Output:
"""
{'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 8500}}      """