# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 16:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriere', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update_at')),
                ('student', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='StudentApp.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Lucrare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titluLucrare', models.CharField(blank=True, max_length=254)),
                ('tipLucrare', models.CharField(blank=True, choices=[('L', 'Licenta'), ('D', 'Disertatie')], max_length=1)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update_at')),
            ],
        ),
        migrations.CreateModel(
            name='LucrareStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=10000)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update_at')),
                ('student', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='StudentApp.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('cnp', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=254)),
                ('last_name', models.CharField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=254)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update_at')),
                ('faculty', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='StudentApp.Facultate')),
            ],
        ),
        migrations.AddField(
            model_name='lucrare',
            name='profesor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ProfessorApp.Professor'),
        ),
        migrations.AddField(
            model_name='lucrare',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.Student'),
        ),
    ]
