# Shirts are large by default 
def make_shirt(size='l', text='i love python'):
    print(f"Your size is '{size.title()}'.\nText on T-Shirt: '{text.title()}'")
make_shirt()

# Medium shirt with the default message
def make_shirt(size='l', text='i love python'):
    print(f"Your size is '{size.title()}'.\nText on T-Shirt: '{text.title()}'")
make_shirt(size='m')

# Shirt of any size with a different message.
def make_shirt(size='l', text='i love python'):
    print(f"Your size is '{size.title()}'.\nText on T-Shirt: '{text.title()}'")
make_shirt(size='s', text='i love my boyfriend')