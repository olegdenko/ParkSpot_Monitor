from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import Plates, Sessions, Balance, BlacklistedVehicle
from .forms import UserAdminChangeForm, UserAdminCreationForm,  PlatesForm, BlacklistedVehicleForm

class BlockUserAdmin(admin.AdminSite):
    site_header = 'Admin Panel'
    

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

@admin.register(BlacklistedVehicle)
class BlacklistedVehicleAdmin(admin.ModelAdmin):
    list_display = ('plate', 'user', 'reason')
    list_filter = ('plate', 'user')
    search_fields = ('plate__plate', 'user__username', 'reason')

class PlatesAdmin(admin.ModelAdmin):
    list_display = ('plate', 'user')

class SessionsAdmin(admin.ModelAdmin):
    list_display = ('plate', 'entrance_time', 'exit_time')

class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

admin_site = BlockUserAdmin(name='block_user_admin')

admin_site.register(User, UserAdmin)
admin_site.register(Plates, PlatesAdmin)
admin_site.register(Sessions, SessionsAdmin)
admin_site.register(Balance, BalanceAdmin)
admin_site.register(BlacklistedVehicle, BlacklistedVehicleAdmin)

