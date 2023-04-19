"""1. A store charges ₹120 per item if you buy less than 10 items. If you buy between 10 and 99 items,
the cost is ₹100 per item. If you buy 100 or more items, the cost is ₹70 per item. Write a program that
asks the user how many items they are buying and prints the total cost.  """


a=int(input("Enter the number of items :: "))
if a<0:
  print("!!!INVALID INPUT!!!")
elif a>=0 and a<10:
  print("Total cost is :: Rs.", a*120)
elif a>=10 and a<100:
  print("Total cost is :: Rs.", a*100)
elif a>=100:
  print("Total cost is :: Rs.", a*70)
