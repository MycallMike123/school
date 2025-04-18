# Generated by Django 5.2 on 2025-04-08 09:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('TEACHER', 'Teacher'), ('PARENT', 'Parent')], max_length=10),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_obtained', models.PositiveIntegerField()),
                ('out_of', models.PositiveIntegerField()),
                ('percentage', models.PositiveIntegerField(editable=False)),
                ('exam_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.teacher')),
            ],
            options={
                'unique_together': {('student', 'subject', 'exam_date')},
            },
        ),
    ]
