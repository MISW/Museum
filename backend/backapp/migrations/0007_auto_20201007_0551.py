# Generated by Django 3.1.1 on 2020-10-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0006_gameinf_link_browser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinf',
            name='submittedtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gameinf',
            name='updatedtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]