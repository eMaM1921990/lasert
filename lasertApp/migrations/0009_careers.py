# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lasertApp', '0008_serivces_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=150, unique=True)),
                ('job_sector', models.CharField(max_length=150)),
                ('years_of_experience', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('job_description', models.TextField()),
                ('job_skills', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('job_mail', models.EmailField(max_length=254)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'careers',
                'managed': True,
                'verbose_name_plural': 'Careers',
            },
        ),
    ]
