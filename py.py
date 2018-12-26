#python try-catch exception
'''
 try catch actually checks code and run
 if any error occurs it shows error as exception and also handles it.
'''

try:
	answer  = 10/0
	number = int(input("Enter a number"))
	print(number)

except ZeroDivisionError as err:
	print(err)
except ValueError:
    print("invalid input")

