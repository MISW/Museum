# Generated by Django 3.1.1 on 2020-10-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0004_auto_20201007_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinf',
            name='link_Android',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gameinf',
            name='link_Mac',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gameinf',
            name='link_Windows',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gameinf',
            name='link_iOS',
            field=models.TextField(blank=True, null=True),
        ),
    ]
