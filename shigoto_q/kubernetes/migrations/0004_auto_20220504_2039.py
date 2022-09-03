# Generated by Django 3.1.7 on 2022-05-04 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("docker", "0001_initial"),
        ("kubernetes", "0003_auto_20220504_2036"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deployment",
            name="image",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="docker.dockerimage"
            ),
        ),
    ]