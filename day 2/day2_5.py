#bill amount calcularor

print("hello and weclome to calculator app")
bill = float(input("enter the amount of bill:$"))
tip = int(input("enter the tip amount 10,12,15:"))
person = int(input("enter the person will spit the bill:"))


percent_tip = tip /100
total_tipp = percent_tip * bill
total_bill = total_tipp + bill
per_person= total_bill/person

final_amount = round(per_person,2)
print(final_amount)

