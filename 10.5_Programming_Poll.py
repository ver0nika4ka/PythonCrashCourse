filename = 'responses.txt'
with open(filename, 'a') as file_object:
    while True:
        print("If you want to exit a program enter 'exit'.")
        response = input("Why do you like programming?\n"
            "Enter your answer: ")
        if response == 'exit':
            break
        else:
            file_object.write(response + '\n')