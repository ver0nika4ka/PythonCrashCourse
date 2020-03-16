# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

multiples_of_three = []
for value in range(3,31,3):
    multiples_of_three.append(value)

# #the same using list comprehensions
multiples_of_three = [value for value in range(3,31,3)]

# the same but using list()
multiples_of_three = list(range(3,31,3))


# finally printing numbers
for number in multiples_of_three:
    print(number)
