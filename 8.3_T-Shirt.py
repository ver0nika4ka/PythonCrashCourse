def make_shirt(size, text):
    print(f"Your size is '{size.title()}'.\nText on T-Shirt: '{text.title()}'")
# Using positional arguments
make_shirt('s', 'i love python')

def make_shirt(size, text):
    print(f"Your size is '{size.title()}'.\nText on T-Shirt:'{text.title()}'")
# Using keyword arguments order doesn't matter
make_shirt(text='i love java', size='m')