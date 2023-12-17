#mesure check code

fname =input("enter your name\n")
sname = input("enter the second name\n")

final_name = fname + sname
lower_case= final_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t+r+u+e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l+o+v+e

love_score = str(true)+str(love)

print(f"your score is {love_score}")