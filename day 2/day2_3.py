#bmi calculator

height = input("Enter the height m: ")
weight = input("Enter the weight:  ")

bmi =    int(weight) /   float(height)   **  2
bmi_as_int = int(bmi)
print(bmi_as_int)
