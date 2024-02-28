height = float(input("enter the height: "))
weight= float(input("enter the height: "))


bmi = round(weight / height **2)

print(bmi)

if bmi < 18.5:
    print("under weight")
elif bmi <25:
    print("normal")
elif bmi < 35:
    print("little over weight")
else:
    print("over weight")