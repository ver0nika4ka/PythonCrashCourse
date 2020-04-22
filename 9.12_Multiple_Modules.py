# from user import User
from privileges_admin import Privileges, Admin

admin_user = Admin('veronica','ivanova','20','belarus')
admin_user.describe_user()
admin_user.greet_user()
admin_user.privileges.show_privileges()