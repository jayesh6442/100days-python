#make program to check cost for roler coster



height = int(input("enter the height: "))

if height > 130:
    print("you  can ride")
else:
    print("you can not")

for i in range(1,7):
    for j in range(i):
        print("* ",end=" ")
    print()