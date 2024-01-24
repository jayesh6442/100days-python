
score = float(input("Enter the student's score: "))

if score >= 90 and score <= 100:
    grade ="a"
elif score >= 80 and score <=89:
    grade = "b"
elif score >= 70 and score <= 79:
    grade = "c"
elif score >=60 and score<= 69:
    grade = "d"
elif score >=50 and score<=59:
    grade = "e"
else:
    
    grade="padai karlo thoda"

print(f"The student's grade is: {grade}")
