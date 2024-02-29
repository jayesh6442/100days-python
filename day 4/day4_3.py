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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("enter 0 for rock 1 for paper 2 for scissors: "))
print("you chose \n",game_images[user_choice])
computer_choice = random.randint(0,2)
print(f"the computer chose",game_images[computer_choice])

if computer_choice == user_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or  (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")