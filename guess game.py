import random
print("welcome to guessing game")
a=random.randint(1,20)
attempt=-5
while True:
   b=int(input("enter a number:"))
   attempt+=1
   if a>b:
      print("too low......")
   elif b>a:
      print("too high...")
   else:
      print("correct answer you took",attempt,"attempts to win......")
      break
