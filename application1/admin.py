from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Custom UserAdmin class to customize the User admin
class CustomUserAdmin(UserAdmin):
    # Add customizations here if needed
    pass

# Unregister the default User model first
admin.site.unregister(User)

# Then register your custom UserAdmin
#admin.site.register(User, CustomUserAdmin)
