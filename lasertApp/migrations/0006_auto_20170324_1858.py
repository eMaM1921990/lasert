# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lasertApp', '0005_auto_20170324_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serivces',
            old_name='description',
            new_name='description_ar',
        ),
        migrations.RenameField(
            model_name='serivces',
            old_name='service_name',
            new_name='service_name_ar',
        ),
        migrations.RenameField(
            model_name='solutions',
            old_name='name',
            new_name='name_ar',
        ),
        migrations.AddField(
            model_name='serivces',
            name='description_en',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]