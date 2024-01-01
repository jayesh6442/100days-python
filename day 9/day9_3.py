student_score = {
    "jayesh": 23,
    "abc": 34,
    "xyz":65,
    "pqy": 23,

}


student_grade = {}



for sutudent in student_score:
    score = student_score[sutudent]
    if score > 34:
        student_grade[sutudent] = "outstanding"
    elif score >23:
        student_grade[sutudent] = "jana bhai"

print(student_grade)