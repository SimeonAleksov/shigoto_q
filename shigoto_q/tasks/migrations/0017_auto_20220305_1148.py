# Generated by Django 3.1.7 on 2022-03-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_usertask_external_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='task_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Simple Http Operator'), (1, 'Kubernetes Operator'), (2, 'Docker Operator')], default=0),
        ),
    ]
