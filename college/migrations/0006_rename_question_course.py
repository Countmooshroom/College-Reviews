# Generated by Django 4.1.3 on 2022-12-13 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_rename_attendance_sum_teacher_attendance_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Course',
        ),
    ]
