# Generated by Django 3.1.7 on 2022-03-05 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_usertask_external_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertask',
            name='external_task_id',
        ),
    ]
