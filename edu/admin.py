from django.contrib import admin

from .models import Classes, Subjects, Lessons
# Register your models here.

admin.site.register(Classes) 
admin.site.register(Subjects) 
admin.site.register(Lessons) 