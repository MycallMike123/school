# Generated by Django 5.2 on 2025-04-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_subject_alter_userprofile_role_teacher_examresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_no',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='full_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='home_county',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='primary_school',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='employee_id',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
