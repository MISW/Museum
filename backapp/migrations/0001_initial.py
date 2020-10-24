# Generated by Django 3.1.2 on 2020-10-06 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categoryInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', models.IntegerField()),
                ('categoryname', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='downloadLinkInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.IntegerField()),
                ('machineid', models.IntegerField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GameCategoryInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.IntegerField()),
                ('categoryid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='gameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.IntegerField()),
                ('player', models.TextField()),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='machineInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machineid', models.IntegerField()),
                ('machinename', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='statusInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusid', models.IntegerField()),
                ('statusname', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gameInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('status', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/gameInf')),
                ('submittedtime', models.DateTimeField()),
                ('updatedtime', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='developPartInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='developerInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
