print("welcome to the tip calculator")

total_bill = float(input("Enter the Total bill: "))
tip = int(input("Enter the Total tip in % 10,12,15: "))
person = int(input("enter how many people will split: "))

bill_with_tip = tip /100 * total_bill + total_bill

print("per person bill: ",bill_with_tip/person)


