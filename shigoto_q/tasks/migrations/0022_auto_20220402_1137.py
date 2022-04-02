# Generated by Django 3.1.7 on 2022-04-02 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shigoto_q.tasks.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0021_auto_20220327_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='DockerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repository', models.CharField(max_length=255, verbose_name='Url of the GitHub repository')),
                ('name', models.CharField(max_length=255, verbose_name='Name of the GitHub repository')),
                ('image_name', models.CharField(help_text='Name of the Docker image inside user namespace', max_length=255, unique=True, verbose_name='Image name')),
                ('command', models.CharField(help_text='Command to execute after image startup.', max_length=255, verbose_name='Command to execute')),
                ('secret_key', models.CharField(blank=True, default=shigoto_q.tasks.models.generate_secret, max_length=512, null=True, unique=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AlterField(
            model_name='usertask',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_usertask_related', related_query_name='tasks_usertasks', to='tasks.dockerimage'),
        ),
        migrations.DeleteModel(
            name='TaskImage',
        ),
    ]