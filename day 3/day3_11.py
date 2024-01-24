print("welcome to price of ticket of roler coster")


age = int(input("enter the age: "))
is_student = input("you are student(yes/no): ").lower()
ticket = 0
if age <=5:
    ticket = 0
elif age >=6 and age<= 12:
    ticket +=10
elif age >=13 and age<=18:
    
    ticket +=15
elif age >=19:
    ticket +=20
else:
    print("enter valid age")

if age >=13 and age <=18 and is_student=="yes":
    ticket-=5

print(f"your fair is: ${ticket}")