from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# в дальнейшем использовать LoginRequiredMixin
def home(request):
    return render(request, "add_base.html")

def students(request):
    return render(request, "for_students.html")

def teachers(request):
    return render(request, "for_teachers.html")
