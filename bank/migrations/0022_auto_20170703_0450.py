# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0021_auto_20170703_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image_1',
            field=models.ImageField(blank=True, default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image_2',
            field=models.ImageField(blank=True, default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image_3',
            field=models.ImageField(blank=True, default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image_4',
            field=models.ImageField(blank=True, default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image_5',
            field=models.ImageField(blank=True, default=False, upload_to=''),
        ),
    ]
