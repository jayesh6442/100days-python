import random
random_word =["jayesh","sarvaiya","hangman"]


the_word = random.choice(random_word)
print(the_word)
blank =''
for _ in range(len(the_word)):
    
    blank+="_, "
print(blank)

user_input= input("enter the geuss: ")




for letter in the_word:
    if letter==the_word:
        print("right")
