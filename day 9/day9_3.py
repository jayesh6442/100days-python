student_grade ={
    "jayesh": 99,
    "akon": 34,
    "idkon": 56,
    "pqt": 67,
    "xya": 53,
    "abx": 23,
}

student_marks = {}

for student in student_grade:
    score = student_grade[student]
    if score > 90:
        student_marks[student] = "kya baat he"
    
print(student_marks)
