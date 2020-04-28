import json

def get_fav_number():
    """Asking person about favourite number."""
    number = input("Enter your favourite number: ")
    filename = 'fav_num.json'
    with open(filename,'w') as f:
        json.dump(number, f)
    return number

get_fav_number()