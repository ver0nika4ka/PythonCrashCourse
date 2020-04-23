"""A class Die with one attribute sides has a default value of 6. 
Method roll_die() prints random num from 1 and num of sides die has. 
Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. """
from random import randint

class Die:
    """This class represents a die with arbitrary number of sides."""

    def __init__(self, sides=6):
        """Initialize a die."""
        self.sides = sides

    def roll_die(self):
        """Print a random number."""
        roll = randint(1, self.sides)
        print(roll)

cubic = Die()
cubic_10 = Die(10)
cubic_20 = Die(20)

# Rolling each die 10 times.
for i in range(10):
    cubic.roll_die()
    cubic_10.roll_die()
    cubic_20.roll_die()

