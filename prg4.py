n=int(input("Enter the value of n :: "))
g1=g2=g3=0
for i in range(1,n+1):
  age=int(input("Enter employee age :: "))
  if(26<=age<=35):
      g1+=1
  elif(36<=age<=45):
      g2+=1
  elif(46<=age<=55):
      g3+=1
print("Employees in age group 26 - 35 :: ",g1)
print("Employees in age group 36 - 45 :: ",g2)
print("Employees in age group 46 - 55 :: ",g3)
