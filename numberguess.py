# User will get 5 chances  number
# Computer will  generate random number
# computer will give hints
# user will the number
from random import randint

computer_num = 0
print("""
    Choose the level of the game ...
      1.Hard
      2.Easy
      3.Medium
""")

level = input().lower()

if level == "hard":
 computer_num = randint(1,100)
elif level == "easy":
  computer_num = randint(1,30)
elif level == "medium":
  computer_num = randint(1,50)


print(computer_num)
chances = 5
won = ""

while chances:
  user_num = int(input("Enter the guess number"))
  if computer_num == user_num:
    won = "yes"
    print("Guess correctly")
    break
  elif computer_num > user_num:
    print("wrong guess number is greater than",computer_num)
  elif computer_num < user_num:
    print("wrong guess number is smaller than",computer_num) 

  chances -=1

if "yes" in won:
  print("You win the game")
else :
  print("You loose the game")