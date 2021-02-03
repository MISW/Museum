# Generated by Django 3.1.5 on 2021-02-03 06:13

import backend.developments.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(0, 'Windows'), (1, 'iOS'), (2, 'Android'), (3, 'ブラウザ'), (4, 'その他')], help_text='0: Windows, 1: iOS, 2: Android, 3: browser, 4: others')),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Link',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(0, '画像'), (1, '音声'), (2, '動画')], help_text='0: image, 1: audio, 2: video')),
                ('file', models.FileField(blank=True, null=True, upload_to=backend.developments.models.get_media_path)),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('associations', models.CharField(blank=True, default='', help_text='0: programming, 1: CG, 2: MIDI', max_length=6, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='associations')),
                ('status', models.IntegerField(choices=[(0, '申請中'), (1, '公開中'), (2, '非公開')], default=0, help_text='0: 申請中, 1: 公開中, 2: 非公開', verbose_name='status')),
                ('is_private', models.BooleanField(default=False, help_text='Open only within misw or not')),
                ('top_image', models.ImageField(blank=True, help_text='top image to be listed to home', null=True, upload_to='developments/images', verbose_name='top_image')),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('co_developers', models.ManyToManyField(blank=True, related_name='development_co_developers', to=settings.AUTH_USER_MODEL)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='development_developer', to=settings.AUTH_USER_MODEL)),
                ('links', models.ManyToManyField(blank=True, related_name='links', to='developments.Link')),
                ('medias', models.ManyToManyField(blank=True, related_name='Medias', to='developments.Media')),
            ],
            options={
                'verbose_name_plural': 'Development',
            },
        ),
    ]
