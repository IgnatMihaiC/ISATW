# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facultate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Specializare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254)),
                ('facultate', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='StudentApp.Facultate')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('cnp', models.IntegerField(unique=True)),
                ('nr_matricol', models.CharField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=254)),
                ('last_name', models.CharField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=254)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update_at')),
                ('specializations', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='StudentApp.Specializare')),
            ],
        ),
    ]
