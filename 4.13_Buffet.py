# Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
buffet_food = ('noodles', 'potato', 'vegetables', 'meat', 'fish')
print('Original menu: ')
for food in buffet_food:
    print(food.title())
# Try to modify one of the items, and make sure that Python rejects the change.
# buffet_food.append = 'shrimp'
# The restaurant changes its menu, replacing two of the items with different foods. 
# Add a line that rewrites the tuple
# Use a for loop to print each of the items on the revised menu.
modified_food = ('noodles', 'potato', 'vegetables', 'bread', 'rice')
print('Modified menu: ')
for m_food in modified_food:
    print(m_food.title())