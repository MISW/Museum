# Generated by Django 3.1.1 on 2020-10-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201006_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='isadmin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
