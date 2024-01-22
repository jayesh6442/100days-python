import random


def card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    chosen = random.choice(cards)
    return chosen


user_card =[]
computer_card =[]

for _ in range(2):
   new_card =  card()
   user_card.append(new_card)
print(user_card)

def score(cards):
   return sum(cards)

for _ in range(2):
    new_card = card()
    computer_card.append(new_card)
print(computer_card)


print(score(computer_card))
print(score(user_card))