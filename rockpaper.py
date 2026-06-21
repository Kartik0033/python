from  random  import choice

l1_choices = ["rock","paper","scissors"]

computer_choice = choice(l1_choices)


d1 = {1:"rock",2:"paper",3:"scissors"}

print("""
  Enter Your Choices:
      1.Rock
      2.Paper
      3.Scissors
""")
user_choices = int(input())

user_choice = d1[user_choices]
print(user_choice)

if user_choice == computer_choice:
  print("HOly shit it's a tie")

if user_choice == "rock" and computer_choice == "scissors":
  print(f"You Win.....Your choice {user_choice} , Computer choice {computer_choice}")
elif user_choice == "paper" and computer_choice == "rock":
  print(f"You Win......Your choice {user_choice} , Computer choice {computer_choice}")
elif user_choice == "scissors" and computer_choice == "paper":
  print("You win")
else :
  print(f"You Loose ..Your choice {user_choice} , Computer choice {computer_choice}")