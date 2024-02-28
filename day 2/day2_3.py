#bmi calculator
height = input("enter the height in meter: ")
weight = input("enter the weight in kg: ")

bmi = int(weight )/ float(height) ** 2
int(bmi)
print(f"your bim is  ${bmi}")