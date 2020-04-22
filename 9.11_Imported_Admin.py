from admin import User, Admin, Privileges

admin_user = Admin('veronica','ivanova','20','belarus')
admin_user.describe_user()
admin_user.greet_user()
admin_user.privileges.show_privileges()

# import admin

# admin_user = admin.Admin('veronica','ivanova','20','belarus')
# admin_user.describe_user()
# admin_user.greet_user()

# admin_user = admin.Privileges()
# admin_user.show_privileges()