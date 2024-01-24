student_hight=input("enter the hight of students: ").split()
print(type(student_hight))
for i in range (0,len(student_hight)):
    student_hight[i]= int(student_hight[i])
print(student_hight)
print(sum(student_hight))
average_height = round(sum(student_hight)/ len(student_hight))
print(f"average height is {average_height}")