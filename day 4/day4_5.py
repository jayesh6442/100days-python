
import random

name_srting = input("enter the name saparate by the ,: ")
op = name_srting.split(",")


for a in op:
    print(a)

cho = random.choice(op)
print(f"the bill will be paid by the {cho}")