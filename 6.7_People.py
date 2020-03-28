person1 = {
        'username': 'asmith',
        'first': 'alex',
        'last': 'smith',
        'age': 30,
        'location': 'new york',
        }
person2 = {
        'username':'vi3tor',
        'first': 'victor',
        'last': 'makov',
        'age': 29,
        'location': 'minsk',
        }
person3 = {
        'username':'tsuzuki',
        'first': 'taro',
        'last': 'suzuki',
        'age': 45,
        'location': 'tokyo',
        }
people = [person1, person2, person3]
# for person in people:
#     print("\nPerson info:")
#     for key, value in person.items():
#         if key == 'username' or key == 'age':
#             print(f"{key.title()}: {value}")
#         else:
#             print(f"{key.title()}: {value.title()}")

for person in people:
    print("\nPerson info:")
    for key, value in person.items():
        if not (key == 'username' or key == 'age'):
            value = value.title()
        print(f"{key.title()}: {value}")