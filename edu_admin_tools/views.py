from django.shortcuts import redirect, render
# from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from users.models import User

def add_schoolers(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        
        for index, row in df.iterrows():
            username = row.get('Логин')
            name = row.get('Имя')
            surname = row.get('Фамилия')
            password = row.get('Пароль')
            patronymic = row.get('Отчество')
            if not isinstance(patronymic, str):
                patronymic = ''
            if username and password and name and surname:
                User.objects.create_user(login=username, password=password, first_name=name, last_name=surname, patronymic=patronymic)
        
        return redirect('home')
    
    return render(request, "tools/add_schoolers.html")  