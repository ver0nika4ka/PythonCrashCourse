prompt = "\nPlease enter pizza tippings you would like: "
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!")
