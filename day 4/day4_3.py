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
user_choise = int(input("enter 0 for rock 1 for paper 2 for scissors: "))
print("you chose \n",game_images[user_choise])
computer_choice = random.randint(0,2)
print(f"the computer chose",game_images[computer_choice])
if computer_choice == user_choise:
    print("its draw")
elif computer_choice > user_choise:
    print("computer win")
else:
    print("user win")