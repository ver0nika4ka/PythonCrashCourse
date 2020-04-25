filename = 'guest.txt'
with open(filename, 'a') as file_object:
    name = input("Enter your name: ")
    file_object.write(name + '\n')

# name = 'Veronica'

# name += '\n'
# string_1 = name + '\n'