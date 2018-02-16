# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunto', '0011_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education_level',
            field=models.PositiveIntegerField(choices=[(1, 'Secondary'), (2, 'Post Secondary')], default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='experience_area',
            field=models.PositiveIntegerField(choices=[(1, 'Technology'), (2, 'Hospitality'), (3, 'Education'), (4, 'Miscellaneous')], default=4),
        ),
        migrations.AddField(
            model_name='profile',
            name='experience_level',
            field=models.PositiveIntegerField(choices=[(1, 'No Experience'), (2, 'Some Experience'), (3, 'Experienced with certification')], default=1),
        ),
    ]