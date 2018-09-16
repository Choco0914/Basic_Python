import admins

admin = admins.Admin('choco', 'amond')
admin.privileges.privileges('delete')
admin.privileges.privileges('create')
admin.describe_user()
admin.privileges.show_privileges()
