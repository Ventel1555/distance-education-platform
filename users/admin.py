from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('login', 'first_name', 'last_name', 'patronymic', 'role', 'classes_id', 'is_active')
    list_filter = ('role', 'classes_id', 'is_active')