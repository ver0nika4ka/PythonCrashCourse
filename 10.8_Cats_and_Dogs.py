def print_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} is missing!")
    else:
        print(f"Contents of {filename}:")
        print(contents.title())


filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'

print_file(filename_1)
print_file(filename_2)









