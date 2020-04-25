filename = 'guest_book.txt'
with open(filename,'a') as file_object:
    while True:
        print("If you want to exit enter 'quit'")
        name = input("Enter your name: ")
        if name == 'quit':
            break
        else:
            print(f"Hello, {name.title()}! Welcome to dinner.")
            file_object.write(name + '\n')
