food = 'sushi'
print("Is this food == 'sushi? I predict True.")
print(food == 'sushi')

print("Is this food == 'pasta'? I predict False.")
print(food == 'pasta')

# Checking if pizza and pasta in list.
food = 'sushi','meat','pizza'

print("Is this food in the list? I predict True.")
print('pizza' in food)

print("Is pasta in the list? I predict False.")
print('pasta' in food)


print("Is pasta NOT in the list? I predict True.")
print('pasta' not in food)

# Checking if age of Victor and Veronica more than 21 y.o.
age_ver = 24
age_vic = 29
print("If age of Victor and Veronica is more than 21, I predict True.")
print(age_vic >= 21 and age_ver >= 21)

print("If age of Victor and Veronica is less than 21, I predict False.")
# You can add extra bracets for more readability
print((age_vic <= 21) and (age_ver <= 21))

print("Is Victor older than Veronica? I predict True")
print(age_vic > age_ver)

print("Is anyone older than 25? I predict True")
print(age_ver > 25 or age_vic > 25)

# Checking for error. 
# I ordered salmon and check if what brought is salmon - ok (False).
# If what brought is not salmon (True, go inside if and print)
sushi = 'tuna'
print("Is sushi == salmon? I predict False")
print(sushi == 'salmon')

code_compiled = True
running_correctly = False
print("Can we move on? I predict False")
print(code_compiled and running_correctly)

