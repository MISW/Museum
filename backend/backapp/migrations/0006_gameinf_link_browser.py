# Generated by Django 3.1.1 on 2020-10-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0005_auto_20201007_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinf',
            name='link_browser',
            field=models.TextField(blank=True, null=True),
        ),
    ]