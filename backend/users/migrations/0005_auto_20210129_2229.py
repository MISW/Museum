# Generated by Django 3.1.4 on 2021-01-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210129_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/User', verbose_name='image'),
        ),
    ]
