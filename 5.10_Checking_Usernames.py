current_users = ['Veronica','Nastya','Victor','Alex','admin']
new_users = ['veronica','nastya','bectur','sema','alla']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

# current_users_lower = [user.lower() for user in current_users]

for n_user in new_users:
    if n_user.lower() in current_users_lower:
        print(f"Please choose another username. Username {n_user} already exists.")
    else:
        print(f"This username {n_user} is avaliable.")
