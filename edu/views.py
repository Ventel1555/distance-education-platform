from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from edu.models import Classes

# в дальнейшем использовать LoginRequiredMixin

# urls for main_html dir
def home(request):
    return render(request, "main_html/add_base.html")

def help_page(request):
    return render(request, "main_html/help_page.html")

# Student
def students(request):
    if request.user.role == 'S':
        return render(request, "main_html/for_students.html")
    else:
        return HttpResponseForbidden()

# Teacher
def teachers(request):
    if request.user.role == 'T':
        return render(request, "main_html/for_teachers.html")
    else:
        return HttpResponseForbidden()

def redaction(request):
    if request.user.role == 'T':
        classes = Classes.objects.filter(id='1',).order_by('id')
        context = {
            'classes': classes,
        }
        return render(request, "teacher/redaction.html", context=context)
    else:
        return HttpResponseForbidden()

# Admin
def admin_panel(request):
    if request.user.role == 'A':
        return render(request, "main_html/for_admin.html")
    else:
        return HttpResponseForbidden()


    