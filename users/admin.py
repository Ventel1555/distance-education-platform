from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('login', 'first_name', 'last_name', 'patronymic', 'role', 'classes_id', 'is_active')
    list_filter = ('role', 'classes_id', 'is_active')
    fields = [('first_name', 'last_name'), 'patronymic', ('login', 'password'), 'email', 'classes_id', 'subjects_id', ('role', 'is_active', 'is_superuser') ]
    search_fields = ["last_name"]
    search_help_text = 'Тут работает поиск пользователя по фамилии'