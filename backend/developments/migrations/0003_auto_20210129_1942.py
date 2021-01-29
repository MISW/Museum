# Generated by Django 3.1.4 on 2021-01-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developments', '0002_auto_20210129_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='type',
            field=models.IntegerField(choices=[(0, 'Windows'), (1, 'iOS'), (2, 'Android'), (3, 'ブラウザ'), (4, 'その他')], help_text='0: Windows, 1: iOS, 2: Android, 3: browser, 4: others'),
        ),
        migrations.AlterField(
            model_name='media',
            name='type',
            field=models.IntegerField(choices=[(0, '画像'), (1, '音声'), (2, '動画')], help_text='0: image, 1: sound, 2: video'),
        ),
    ]
