#word list and we will make it sore an complete till day 50 today and make it happen


word_list = ["jayehs","sarvaiya","hold"]

import random

chosen_word = random.choice(word_list)


guess =input("enter the word").lower()


for letter in chosen_word:
    if letter ==guess:
        print("right")
    else:
        print("worng")

#we need to revisti this day i skipped it because i was bored 
        