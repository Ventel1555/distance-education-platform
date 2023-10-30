from typing import Any
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from .models import Lessons
# в дальнейшем использовать LoginRequiredMixin
# urls for main_html dir
def home(request):
    return render(request, "main_html/add_base.html")

def help_page(request):
    return render(request, "main_html/help_page.html")

class DetailLessonView(DetailView):
    model = Lessons
    

# Student
def students(request):
    if request.user.role == 'S':
        return render(request, "main_html/for_students.html")
    else:
        return HttpResponseForbidden()

# Teacher
def teachers(request):
    if request.user.role == 'T':
        return render(request, "main_html/for_teachers.html")
    else:
        return HttpResponseForbidden()

def redaction(request):
    if request.user.role == 'T':
        subjects = request.user.subjects_id.all()
        sub_name = request.GET.get('sub_name') or None
        if sub_name != None:
            lessons = subjects.get(name=sub_name).lesson_id.all()
            pass
        # if  sub_name != None:
            # if (int(sub_name[-2]), sub_name[-1]):
            #     subjects = Subjects.objects.filter(pk__in=request.user.subjects_id.all().values_list('id', flat=True) )
            #     sub_name = Classes.objects.filter(number=int(sub_name[0]), letter=sub_name[1:])
            # else:
            #     return HttpResponseForbidden()
        #     print(b.split(' ')[1][-1])
        # print(b.split(' ')[1][0:-1])

            # прописать доступы к классам. И развертовани с поиском предметов.
            # Дальше админом пользуемся (создание через excel предметов, уроков и классов, учителей и учиников)
            # Добавление учителей с привзякой прдметов и классво на сайте 
            # (я предмсвтлю выборку именно прдеметов, и понима автоматическое распредедение по классам)
            # как только сделаем прлое можео думать о редактирвани дз ит..д
        context = {
            'lessons': None if sub_name==None else lessons,
            'subjects': subjects,
            'active_sub': sub_name,
            }
        return render(request, "teacher/redaction.html", context=context)
    else:
        return HttpResponseForbidden()

# Admin
def admin_panel(request):
    if request.user.role == 'A':
        return render(request, "main_html/for_admin.html")
    else:
        return HttpResponseForbidden()


    