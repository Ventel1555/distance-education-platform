from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edu/detail-lesson/<int:pk>', views.DetailLessonView.as_view(template_name="detail_lesson.html"), name='detail_lesson'),
    path('students/homework-list', views.list_homework_view, name='homework-list'),
    path('teachers/redaction', views.redaction, name='redaction_teachers'),
]
