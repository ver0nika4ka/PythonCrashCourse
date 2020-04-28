import json

filename = 'fav_num.json'   

try:
    with open(filename) as f:
        fav_num = json.load(f)
except FileNotFoundError:
    number = input("Enter your favourite number: ")
    with open(filename,'w') as f:
        json.dump(number, f)
    print("Thank you, I will remember it next time!")
else:
    print(f"I know your favourite number! It's {fav_num}!")
