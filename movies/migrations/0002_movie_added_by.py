# Generated by Django 4.1.3 on 2022-12-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="added_by",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]