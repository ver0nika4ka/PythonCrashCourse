favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       'victor': 'java',
       'veronica': 'python',
       }
names = ['jen','victor','veronica','alla','nastya','andrei']
for name in names:
    if name in favorite_languages:
        print(f"Thank you for responding, {name.title()}!")
    else:
        print(f"Hi {name.title()}, I invite you to the poll!")