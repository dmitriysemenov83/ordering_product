from django.contrib import admin

from users.models import User


# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'phone', 'country',
                    'avatar', 'is_superuser', 'is_staff', 'is_active']
    search_fields = ['username', 'first_name', 'last_name', 'email',]
    fields = [
        'first_name',
        'last_name',
        'email',
        'avatar',
        'is_active',
        'is_staff',
        ('date_joined', 'last_login'),
        'groups',
        'user_permissions'
    ]