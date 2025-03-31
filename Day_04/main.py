import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
game_input = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_input = random.randint(a=0,b=1)
if user_input >=0 and user_input <=2:
    print(game_input[user_input])
    print(f"computer choice: ")
    print(game_input[computer_input])

if user_input > 2 and user_input < 0:
    print("You have enter invalid number you lose!")
elif user_input == 0 and computer_input == 2:
    print("You Win!")
elif computer_input == 0 and user_input == 2:
    print("You loss!")
elif user_input == computer_input:
    print("It's a Draw!")
elif user_input > computer_input:
    print("You win!")
elif computer_input > user_input:
    print("computer win!")