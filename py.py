#python reading a file

employee_file = open("employees.txt", "a") #"a means append a line in a existing file"
employee_file.write("\nTeacher - Khayrul Islam")
employee_file.close()
