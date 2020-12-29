# Generated by Django 3.1.4 on 2020-12-28 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkInf',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(1, '画像'), (2, '音声'), (3, '動画'), ('URL', ((41, 'Windows'), (42, 'iOS'), (43, 'Android'), (44, 'browser'), (45, 'others')))], help_text='1: image, 2: sound, 3: video, 4: URLS(41: Windows, 42: iOS, 43: Android, 44: browser, 45: others)')),
                ('link', models.URLField(blank=True, null=True)),
                ('file', models.FileField(upload_to='files/DeveloperInf')),
            ],
            options={
                'verbose_name_plural': 'LinkInf',
            },
        ),
        migrations.CreateModel(
            name='DevelopmentInf',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('status', models.IntegerField(default=0, help_text='0: 申請中, 1: 公開中, 2: 非公開', verbose_name='status')),
                ('is_public', models.BooleanField(default=False, help_text='Open only within misw or not')),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('associations', models.ManyToManyField(related_name='developmentinf_associations', to='users.Association')),
                ('links', models.ManyToManyField(to='models.LinkInf')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='developmentinf_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('users', models.ManyToManyField(related_name='developmentinf_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'DevelopmentInf',
            },
        ),
    ]