from django.db import models

# settings.AUTH_USER_MODEL      -   better practise

class Lessons(models.Model):
    data = models.DateField(verbose_name='Дата')
    is_done = models.BooleanField(verbose_name='Урок проведен')
    topic = models.CharField(max_length=40, verbose_name='Тема урока')
    home_work = models.CharField(max_length=40, verbose_name='Домашняя работа')
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.topic


class Subjects(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    lesson_id = models.ManyToManyField(Lessons, verbose_name='Уроки')
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
    
    
class Classes(models.Model):
    number = models.CharField(max_length=1, verbose_name='Номер класса')
    letter = models.CharField(max_length=1, verbose_name='Параллель')
    sub_id = models.ManyToManyField(Subjects, verbose_name='Предметы')
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ["id"]
        
    def get_class(self):
        return self.number + self.letter
        
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.number + self.letter