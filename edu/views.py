from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from edu.models import Classes, Subjects

# в дальнейшем использовать LoginRequiredMixin

# urls for main_html dir
def home(request):
    return render(request, "main_html/add_base.html")

def help_page(request):
    return render(request, "main_html/help_page.html")

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
        user_class = request.user.classes_id.all()
        classes = Classes.objects.filter(pk__in=user_class.values_list('id', flat=True))
        class_name = request.GET.get('class_name') or None
        if class_name != None:
            if (int(class_name[0]), class_name[1:]) in user_class.values_list('number', 'letter'):
                sub_access = Classes.objects.all()
                print(sub_access)
                subjects = Subjects.objects.filter(pk__in=request.user.subjects_id.all().values_list('id', flat=True) )
                class_name = Classes.objects.filter(number=int(class_name[0]), letter=class_name[1:])
            else:
                return HttpResponseForbidden()
            # прописать доступы к классам. И развертовани с поиском предметов.
            # Дальше админом пользуемся (создание через excel предметов, уроков и классов, учителей и учиников)
            # Добавление учителей с привзякой прдметов и классво на сайте 
            # (я предмсвтлю выборку именно прдеметов, и понима автоматическое распредедение по классам)
            # как только сделаем прлое можео думать о редактирвани дз ит..д
        context = {
            'classes': classes,
            'subjects': None if class_name == None else subjects,
            'active_class': None if class_name == None else class_name[0],
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


    