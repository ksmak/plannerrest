from django.contrib import admin
from auths.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'management',
        'department',
        'job',
        'is_active',
    ]

admin.site.register(CustomUser, CustomUserAdmin)
