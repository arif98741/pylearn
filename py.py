#python reading a file

employee_file = open("employees.txt", "r")
#print(employee_file.readlines())
#print(employee_file.readline())
employees = employee_file.readlines()

for index in range(len(employees)):
	print(employees[index])
employee_file.close()
