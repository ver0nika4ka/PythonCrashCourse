# Make a copy of the list of pizzas, and call it friend_sushi 
my_sushi = ['salmon','yellowtail','shrimp', 'tuna']
friend_sushi = my_sushi[:]
my_sushi.append('fatty salmon')
friend_sushi.append('natto')
print("I love sushi very much! Here is my list: ")
for s in my_sushi:
    print(s)
print("My friend loves sushi too. Here is his list: ")
for f in friend_sushi:
    print(f)