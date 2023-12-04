from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
from tablib import Dataset
from .resources import UserResources
from users.models import User


def add_schoolers(request):
    if request.method == 'POST':
        pass    
    return render(request, "tools/add_schoolers.html")  