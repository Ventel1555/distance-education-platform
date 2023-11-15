from django.shortcuts import render
# from django.views.generic import DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseForbidden
# from .models import Lessons

# в дальнейшем использовать LoginRequiredMixin
# urls for main_html dir
def add_schoolers(request):
    return render(request, "add_schoolers.html")