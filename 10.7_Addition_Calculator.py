print("Enter two numbers and I will show the addition result.")

while True:
    num_1 = input("Enter a number and press 'enter': ")
    num_2 = input("Enter a second number and press 'enter': ")
    try:
        result = int(num_1) + int(num_2)
    except ValueError:
        print("Please enter two numbers!")
    else:
        print(f"The result is: {result}")

        