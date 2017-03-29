# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lasertApp', '0009_careers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'subscribers',
                'managed': True,
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.AlterModelOptions(
            name='careers',
            options={'managed': True, 'ordering': ['-create_date'], 'verbose_name_plural': 'Careers'},
        ),
    ]
