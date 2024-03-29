file_name = input("File Name: ")
class_name = input("Class Name: ")

if class_name != None:
    grade = input("Grade: ")
    credits = input("Credits: ")
    f = open(file_name, "a")
    while class_name != "":
        class_info = (class_name + ":" + grade + ":" + credits + " ")
        f.write(class_info)
        class_name = input("Class Name: ")
        grade = input("Grade: ")
        credits = input("Credits: ")
f.close   
