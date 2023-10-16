from django.db import models

# settings.AUTH_USER_MODEL      -   better practise
class Classes(models.Model):
    number = models.SmallIntegerField(verbose_name='Номер класса')
    letter = models.CharField(max_length=1)


class Subjects(models.Model):
    name = models.CharField(max_length=20)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)


class Lessons(models.Model):
    data = models.DateField(verbose_name='Дата')
    is_done = models.BooleanField(verbose_name='Урок проведен')
    topic = models.CharField(max_length=40)
    home_work = models.CharField(max_length=40)
    sub_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    