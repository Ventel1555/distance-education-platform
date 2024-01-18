from django.shortcuts import redirect, render
import pandas as pd
from edu.models import Classes
from users.models import User
from .forms import LessonsForm


def add_schoolers(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        role = request.POST.get('Role')
        
        for index, row in df.iterrows():
            username = row.get('Логин')
            name = row.get('Имя')
            surname = row.get('Фамилия')
            password = row.get('Пароль')
            patronymic = row.get('Отчество')
            if not isinstance(patronymic, str):
                patronymic = ''
            if username and password and name and surname:
                User.objects.create_user(login=username, password=password, first_name=name, last_name=surname, patronymic=patronymic, role=role)
        
        return redirect('home')
        
    return render(request, "tools/add_schoolers.html")  


def edu_program(request):
    if request.method == 'POST':
        form = LessonsForm(request.POST)
        return redirect('homework-list')
    else:
        form = LessonsForm()
    return render(request, 'tools/edu_program.html', {'form': form})


def class_change(request):
    students = User.objects.filter(role='S')
    classes = Classes.objects.all()
    if request.method == 'POST':
           selected_students = request.POST.getlist('selected_students')
           class_name= int(request.POST.get('class_filter'))
           print(class_name)
           for selection in selected_students: 
                User.objects.filter(pk=int(selection)).update(classes_id=class_name)
    return render(request, 'tools/class_change.html', {'students': students, 'classes': classes})

