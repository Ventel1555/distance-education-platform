from django.urls import path

from mycrm import views

urlpatterns = [
    path('', views.home, name='home'),
]
