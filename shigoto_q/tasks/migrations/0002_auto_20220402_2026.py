# Generated by Django 3.1.7 on 2022-04-02 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usertask",
            old_name="task_type",
            new_name="type",
        ),
    ]