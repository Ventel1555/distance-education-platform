from django.contrib import admin

from .models import Classes, Subjects, Lessons

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    pass

@admin.register(Subjects)
class Subjectsdmin(admin.ModelAdmin):
    pass

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('topic', 'email', 'data', 'is_done')
    list_filter = ('data', 'is_done', 'email')
