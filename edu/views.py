from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

# в дальнейшем использовать LoginRequiredMixin

# urls for main_html dir
def home(request):
    return render(request, "main_html/add_base.html")

def students(request):
    if request.user.role == 'S':
        return render(request, "main_html/for_students.html")
    else:
        return HttpResponseForbidden()

def teachers(request):
    if request.user.role == 'T':
        return render(request, "main_html/for_teachers.html")
    else:
        return HttpResponseForbidden()

def help_page(request):
    return render(request, "main_html/help_page.html")

def admin_panel(request):
    if request.user.role == 'A':
        return render(request, "main_html/for_admin.html")
    else:
        return HttpResponseForbidden()

# urls for students dir
# def list_homework(request):
#     return render(request, "students/list_homework.html")