from django.urls import path

from . import views

urlpatterns = [
    path('add-schoolers/', views.add_schoolers, name='add_schoolers'),
    path('edu-program/', views.edu_program, name='edu_program'),
    path('class-change/', views.class_change, name='class_change'),
]
