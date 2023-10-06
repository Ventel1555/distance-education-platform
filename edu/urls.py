from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='for_students'),
    path('teachers/', views.teachers, name='for_teachers'),
    path('help-page/', views.help_page, name='help_page'),
    path('admin-panel/', views.admin_panel, name='for_admin'),
]
