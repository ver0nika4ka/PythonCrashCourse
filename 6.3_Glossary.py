glossary = {'list': 'an array of any object',
            'len()': 'function to calculate length',
            'tuples': 'list which you can not change',
            'slicing': 'to determine how to slice the sequence',
            'dictionary': 'similar to a list, but connect pieces as key-value pairs'}
names = ['list', 'len()', 'tuples', 'slicing', 'dictionary']
for name in names:
    print(f"{name.title()} – {glossary[name]}.")