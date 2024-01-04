student_hight=input("enter the hight of students").split()
for n in range (0,len(student_hight)):
    student_hight[n]=int(student_hight[n])
print (student_hight)

total_hight=0
for hight in student_hight:
    total_hight+=hight
print(total_hight)

no_of_student = 0
for student in student_hight:
    no_of_student+=1
print(no_of_student)


avarage_hight = round(total_hight/no_of_student)

print(f"average hight is {avarage_hight}")