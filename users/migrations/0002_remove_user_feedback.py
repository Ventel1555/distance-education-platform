# Generated by Django 5.0.3 on 2024-04-01 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='feedback',
        ),
    ]
