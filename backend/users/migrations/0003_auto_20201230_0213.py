# Generated by Django 3.1.4 on 2020-12-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201230_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='associations',
            field=models.ManyToManyField(default=[], related_name='associations', to='users.Association'),
        ),
    ]