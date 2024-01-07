print("welcome to tip calculator")

amount = float(input("enter the total amount of bill"))

tip = int(input("enter the tip amont in persentage"))

person = int(input("enter how many people will split bill"))

final_bill = tip /100 * amount +amount

per_person=  final_bill / person

final_amount = "{:.2f}".format(per_person)

print(f"per person bill is {final_amount}")