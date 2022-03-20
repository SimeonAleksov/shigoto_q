# Generated by Django 3.1.7 on 2022-03-05 11:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_auto_20220226_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='external_task_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
