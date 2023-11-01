from django.shortcuts import render
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

class DetailLessonView(LoginRequiredMixin, DetailView):
    model = Lessons
    
# Student
def students(request):
    if request.user.role == 'S':
        return render(request, "main_html/for_students.html")
    else:
        return HttpResponseForbidden()

def list_homework_view(request):
    if request.user.role != 'T':
        subjects = request.user.classes_id.sub_id.all()
        sub_name = request.GET.get('sub_name') or None
        if sub_name != None:
            lessons = subjects.get(name=sub_name).lesson_id.filter(is_done =True)
            pass
        context = {
            'lessons': None if sub_name==None else lessons,
            'subjects': subjects,
            'active_sub': sub_name,
            }
        return render(request, "student/list_homework.html", context=context)
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


    