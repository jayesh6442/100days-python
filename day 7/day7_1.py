import random 
word_list = [ 'jayesh', 'and','python']

rand = random.choice(word_list)
print(rand)




display = []
for _ in range(len(rand)):
    display+="_"
print(display)


user_choice = input("enter the choise")

if user_choice == rand:
    print("you chose right")
else:
    print("you chose wrong")