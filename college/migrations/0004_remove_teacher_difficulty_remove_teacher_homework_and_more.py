# Generated by Django 4.1.3 on 2022-12-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_remove_teacher_attendance_remove_teacher_essays_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='homework',
        ),
        migrations.AddField(
            model_name='teacher',
            name='difficulty_sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='homework_sum',
            field=models.IntegerField(default=0),
        ),
    ]
