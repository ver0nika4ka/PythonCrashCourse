# Tests for equality and inequality with strings
pen = 'parker'
print("If pen == 'parker', I predict True")
print(pen == 'parker')
print("If pen != 'parker', I predict False")
print(pen != 'parker')

pensil = 'tombow'
print("If pensil == 'tombow', I predict True")
print(pensil == 'tombow')
print("If pensil == 'mitsubishi', I predict False")
print(pensil == 'mitsubishi')

# Tests using the lower() method
car = 'Toyota'
print(car.lower())
print(car)

# Tests using the and keyword and the or keyword
age_veron = 24
age_victor = 29
print("If V and V older than 21, I predict true.")
print(age_victor > 21 and age_veron > 21)
print("If at least anyone older than 21, I predict true.")
print(age_victor > 21 or age_veron > 21)

# Test whether an item is in a list
drinks = ['water','coffee','tea','juce']
print("If 'tea' in a list, I predict true.")
print('tea' in drinks)
print("If 'sake' in a list, I predict false.")
print('sake' in drinks)

# Test whether an item is not in a list
juces = ['orange','pineapple','grape', 'tomato']
print("If 'apple' NOT in a list, I predict true.")
print('apple' not in juces)
print("If 'tomato' NOT in a list, I predict false.")
print('tomato' not in juces)