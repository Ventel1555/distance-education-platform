# Generated by Django 5.0.3 on 2024-03-18 18:31

import django.db.models.deletion
import users.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('login', models.CharField(max_length=18, unique=True, verbose_name='Логин')),
                ('email', models.EmailField(blank=True, max_length=28, verbose_name='Почта')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=30, verbose_name='Отчество')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('role', models.CharField(blank=True, choices=[('S', 'Ученик'), ('T', 'Учитель'), ('A', 'Администратор')], max_length=8, verbose_name='Роль')),
                ('feedback', models.BooleanField(default=False, verbose_name='Доступ к обрат. связи')),
                ('classes_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Класс', to='edu.classes', verbose_name='Доступы к классу')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('subjects_id', models.ManyToManyField(blank=True, to='edu.subjects', verbose_name='Доступы к предметам')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['last_name'],
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
