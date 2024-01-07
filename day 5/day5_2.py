student_hight=input("enter the hight of students").split()
for n in range (0,len(student_hight)):
    student_hight[n]=int(student_hight[n])
print (student_hight)
print(sum(student_hight))
avarage_hight = round(sum(student_hight)/len(student_hight))
print(f"average hight is {avarage_hight}")