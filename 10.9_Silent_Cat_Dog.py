def print_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"Contents of {filename}:")
        print(contents.title() + '\n')

filenames = ['cats.txt', 'dogs.txt','responses.txt']
for file in filenames:
    print_file(file)