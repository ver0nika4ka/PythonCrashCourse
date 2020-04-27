def print_the_from_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        num_the = contents.lower().count('the ')
        print(f"There are {num_the} 'the' in file {filename}")


print_the_from_file('japanese_girls_and_women.txt')