# Generated by Django 3.0.6 on 2022-08-22 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0008_auto_20220815_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]