# Generated by Django 3.2.8 on 2021-11-08 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='category',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='content',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
