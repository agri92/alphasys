# Generated by Django 3.0.6 on 2022-09-12 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_auto_20220906_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='session_end',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='session_start',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='courses',
            name='detalles',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
    ]
