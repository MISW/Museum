# Generated by Django 3.1.1 on 2020-10-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_isadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='isadmin',
            field=models.BooleanField(default=False, help_text='administrative authority for this user.', verbose_name='isadmin'),
        ),
    ]
