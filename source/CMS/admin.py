from django.contrib import admin
from .models import Complaint, User, Admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'is_staff', 'date_joined']
    search_fields = ['username', 'email']
    list_filter = ['is_staff', 'is_active']

# Register your models here.
admin.site.register(Complaint)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Admin)