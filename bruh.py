from multiprocessing import Value
import random
a = random.randint(0,20)
g=0
while True:
  try:
    userInput = int(input("Enter a number: "))       
  except ValueError:
    print("Not an integer!")
  else:
    print("Yes an integer!")
    break
print(g)
  
 