import matplotlib.pyplot as plt

# Нижние значения засечки количество (values)
input_values = [1, 2, 3, 4, 5]
# Use squares as y - ordinate, and indexes as x - coordinate (0,1,2,3,4)
squares = [1, 4, 9, 16, 25]

# To use style, add this code before starting to generate the plot 
# There are dif styles, to check use import matplotlib.pyplot as plt -> plt.style.available
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels (less ticks)
# ax.tick_params(axis='both', labelsize=14)

plt.show()