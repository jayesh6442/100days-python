#pizz order app


print("Welcome to pizza")
size = input("enter the size:")


add_paperoni = input("do you want extra paperone y of n:")
extra_chees = input("do you want extra chees y or n:")



bill = 0


if size =="s":
    bill+=10
elif size =="m":
    bill=-20
elif size  =="l":
    bill+=30
else:
    print("enter the valid size:")

if add_paperoni=="y":
    if size =="s":
        bill +=5
    else:
        bill +=10
if extra_chees =="y":
    if size =="s":
        bill+=10
print(f"your totoal bill is {bill}")
