# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itaiching', '0002_auto_20161012_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taichimove',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='taichiset',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='taichistyle',
            name='remarks',
        ),
        migrations.AlterField(
            model_name='taichimove',
            name='description',
            field=models.CharField(max_length=200, verbose_name='要求'),
        ),
        migrations.AlterField(
            model_name='taichimove',
            name='num',
            field=models.IntegerField(default=0, verbose_name='第幾動'),
        ),
        migrations.AlterField(
            model_name='taichimove',
            name='title',
            field=models.CharField(max_length=200, verbose_name='口訣'),
        ),
        migrations.AlterField(
            model_name='taichiset',
            name='description',
            field=models.CharField(max_length=200, verbose_name='說明'),
        ),
        migrations.AlterField(
            model_name='taichiset',
            name='num',
            field=models.IntegerField(default=0, verbose_name='第幾式'),
        ),
        migrations.AlterField(
            model_name='taichiset',
            name='title',
            field=models.CharField(max_length=200, verbose_name='名稱'),
        ),
        migrations.AlterField(
            model_name='taichistyle',
            name='description',
            field=models.CharField(max_length=200, verbose_name='說明'),
        ),
        migrations.AlterField(
            model_name='taichistyle',
            name='title',
            field=models.CharField(max_length=200, verbose_name='線路名稱'),
        ),
    ]
