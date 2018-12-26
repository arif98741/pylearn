
def power_maker(base_number,power):
	result = 1
	for index in range(power):
		result = result * base_number
	return result
	
#4^4 = 4 x 4 x 4 x 4


print(power_maker(4,4))
#exponent of number in python
