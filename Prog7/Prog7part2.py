import os
file_name = input("File Name: ")
total_credits = 0
final_grade = 0
num_grade = 0
try:
    student_file = open(file_name, "r")
    for x in student_file:
        credits = int(x[-2])
        total_credits = total_credits + credits
        print(f"{x: <100}")
        grade = x[-4]
        if grade == "A":
            num_grade = credits * 4
        if grade == "B": 
            num_grade = credits * 3
        if grade == "C":
            num_grade = credits * 2
        if grade == 'D':
            num_grade = credits * 1
        if grade == 'F':
            num_grade = credits * 0
        final_grade = final_grade + num_grade
    GPA = final_grade / total_credits
    print("%.2f" % GPA)
except:
    print("File not detected")
