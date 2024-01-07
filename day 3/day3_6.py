height = int(input("enter  the height "))
age = int(input("enter the age "))

if height > 120:
    print("you can ride")
    if age >  18:
        print("fair is 12")
    elif age < 12:
        print("fair is 5")
    elif age < 18 and age > 12:
        print("fair is 7")
else:
    print("you cant ride")
