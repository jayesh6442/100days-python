import random
choice = random.randint(0,1)
if choice == 1:
    print("heads")
else:
    print("tails")


list1 = [1,2,3,"name",45]
for i in list1:
    print(i)
print(len(list1))
#print(list1[8])  will give error like out of the range
#lets make nested list
list2 = [list1,4,5,6,4,3]
print(list2)
choise2= random.randint(1,100)
print(choise2)

