#Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

multiply = []
for value in list(range(3,31)):
	number = value * 3
	multiply.append(number)
	print(number)
print(multiply)

