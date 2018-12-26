#python reading a file

employee_file = open("employees.txt", "r")
print(employee_file.readline())
employee_file.close()
