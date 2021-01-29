# Generated by Django 3.1.4 on 2021-01-29 11:21

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('developments', '0005_auto_20210129_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='development',
            name='associations',
            field=models.CharField(blank=True, choices=[(1, 'プログラミング'), (2, 'CG'), (3, 'MIDI')], default='', help_text='1: programming, 2: CG, 3: MIDI', max_length=200, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
