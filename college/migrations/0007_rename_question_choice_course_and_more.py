# Generated by Django 4.1.3 on 2022-12-13 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_rename_question_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='question_text',
            new_name='course_name',
        ),
    ]
