#bill amount calcularor

print("hello and weclome to calculator app")
bill = float(input("enter the amount of bill:$ "))
tip = int(input("enter the tip amount 10,12,15: "))
person = int(input("enter the person will spit the bill: "))

bill_with_tip = tip / 100 * bill + bill

per_person = round(bill_with_tip / person,2)

print(f"each person get {per_person} to pay")