# Print contents by reading in the entire file
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents.strip())
print("\n")

# Print contents by looping over the file object
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
print("\n")

# Print contents by storing the lines in a list 
# and then working with them outside the with block.
filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

py_knowledge = ''
for line in lines:
    py_knowledge += line.strip()

print(py_knowledge)
print("\n")
