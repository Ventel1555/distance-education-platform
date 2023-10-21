from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/info', views.students, name='for_students'),
    path('teachers/info', views.teachers, name='for_teachers'),
    path('teachers/redaction', views.redaction, name='redaction_teachers'),
    path('help-page/', views.help_page, name='help_page'),
    path('admin-panel/info', views.admin_panel, name='for_admin'),
]
