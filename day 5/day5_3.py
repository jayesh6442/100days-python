#find maximun from list


student_score = input("enter the marks ").split()
for n in range(0,len(student_score)):
    student_score[n]=int(student_score[n])
print(student_score)
high_socre=0

for score in student_score:
    if score > high_socre:
        high_socre = score
print(high_socre) 