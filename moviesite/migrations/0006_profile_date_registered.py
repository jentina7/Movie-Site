# Generated by Django 5.1.1 on 2024-10-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("moviesite", "0005_alter_movie_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_registered",
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
