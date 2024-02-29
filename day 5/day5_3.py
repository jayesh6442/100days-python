# #find maximun from list


# student_score = input("enter the marks ").split()
# for n in range(0,len(student_score)):
#     student_score[n]=int(student_score[n])
# print(student_score)
# print(max(student_score))




score = input("enter the marks: ").split()


for i in range(0,len(score)):
    score[i] = int(score[i])

print(f"The maximum marks is: ",max(score))