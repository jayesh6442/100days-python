# student_hight=input("enter the hight of students: ").split()
# print(type(student_hight))
# for i in range (0,len(student_hight)):
#     student_hight[i]= int(student_hight[i])
# print(type(student_hight))
# print(sum(student_hight))
# average_height = round(sum(student_hight)/ len(student_hight))
# print(f"average height is {average_height}")



student_height = input("enter the height ").split()



for i in range(0,len(student_height)):
    student_height[i] = int(student_height[i])
print(f"The total sum of the all height",sum(student_height))
avarage_height =   round(sum(student_height)/ len(student_height))
print(f"The avarage height is: ",avarage_height)