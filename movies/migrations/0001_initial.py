# Generated by Django 4.1.3 on 2022-12-06 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(max_length=10, null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "General"),
                            ("PG", "Parental Guidance"),
                            ("PG-13", "Parents Strongly"),
                            ("R", "Restricted"),
                            ("NC-17", "Adults Only"),
                        ],
                        default="G",
                        max_length=20,
                    ),
                ),
                ("synopsis", models.TextField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]