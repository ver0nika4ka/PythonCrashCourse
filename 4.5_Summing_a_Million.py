# Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = []
for number in range(1, 1000001):
	numbers.append(number)
print(f"Minimal number is: {min(numbers)}")
print(f"Maximal number is: {max(numbers)}")
print(f"The sum from min and max number is: {sum(numbers)}")



