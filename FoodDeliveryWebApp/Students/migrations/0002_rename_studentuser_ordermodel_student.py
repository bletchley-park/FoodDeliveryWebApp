# Generated by Django 4.1.4 on 2023-05-20 12:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Students", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ordermodel",
            old_name="StudentUser",
            new_name="student",
        ),
    ]
