import random
print("welcome to guessing game")
a=random.randint(1,10)
attempt=0
while True:
   b=int(input("enter a number:"))
   if a>b:
      print("too low")
   elif b>a:
      print("too high")
   else:
      print("correct answer")
