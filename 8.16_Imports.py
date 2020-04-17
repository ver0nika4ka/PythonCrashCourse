import printing_functions

print("Making your sandwich: ")
printing_functions.make_sandwich('cheese')

from printing_functions import make_sandwich

make_sandwich('cheese', 'tomato')

from printing_functions import make_sandwich as ms

ms('cheese', 'tomato', 'mushrooms')

import printing_functions as pf

pf.make_sandwich('cheese', 'tomato', 'mushrooms', 'ham')

from printing_functions import *

make_sandwich('cheese', 'tomato', 'mushrooms', 'ham', 'green peppers')
make_pizza(16, 'mushrooms', 'ham', 'green peppers', 'extra cheese')

print("\nInfo about your car: ")
print(car_info('suzuki', 'lapin'))