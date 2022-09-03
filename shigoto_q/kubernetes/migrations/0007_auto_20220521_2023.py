# Generated by Django 3.1.7 on 2022-05-21 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kubernetes", "0006_deployment_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="namespace",
        ),
        migrations.CreateModel(
            name="Namespace",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="default", max_length=512)),
                ("deployments", models.ManyToManyField(to="kubernetes.Deployment")),
                (
                    "ingress",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="kubernetes.ingress",
                    ),
                ),
                ("services", models.ManyToManyField(to="kubernetes.Service")),
            ],
        ),
    ]