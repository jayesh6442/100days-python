height = float(input("enter the height"))
weight = float(input("enter the weight"))

bmi = weight / height ** 2 
round(bmi)

if bmi < 18.5:
    print("underweight")
elif  bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else:
    print("no condition met")