import json

filename = 'fav_num.json'
with open(filename) as f:
    fav_num = json.load(f)

print(f"I know your favourite number! It's {fav_num}!")