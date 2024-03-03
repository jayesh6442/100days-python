import random
word_list = ["jayesh","viral","savan"]
word=random.choice(word_list)
print(word)

blanck=[]
for _ in range(len(word)):
    blanck+="_"
print(blanck)

end_of_game  = False

while not end_of_game:
    guess = input("Enter the word: ").lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            blanck[position] = letter
   
    print(blanck)
    if "_" not in blanck:
        end_of_game= True
print("you win")