from django.contrib import admin

from users.models import Plates, Sessions


class BlockUserAdmin(admin.AdminSite):
    site_header = 'Admin Panel'
    

admin_site = BlockUserAdmin(name='block_user_admin')

admin_site.register(Plates)
admin_site.register(Sessions)
# admin_site.register(BlacklistedVehicle)

