# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10).
# Use a for loop to print out the value of each cube.
cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

print(cubes)