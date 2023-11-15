from django.urls import path

from . import views

urlpatterns = [
    path('add-schoolers/', views.add_schoolers, name='add_schoolers'),
]
