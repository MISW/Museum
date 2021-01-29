from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.users.models import Association
from backend.users.models import User

MEDIA_CHOICES = (
    (1, '画像'),
    (2, '音声'),
    (3, '動画')
)

LINK_CHOICES = (
    (1, 'Windows'),
    (2, 'iOS'),
    (3, 'Android'),
    (4, 'ブラウザ'),
    (5, 'その他')
)

class Media(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)

    type = models.IntegerField(
        choices=MEDIA_CHOICES,
        help_text='1: image, 2: sound, 3: video'
    )

    file = models.FileField(
        upload_to='files/Development',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.get_type_display()


class Link(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)

    type = models.IntegerField(
        choices=LINK_CHOICES,
        help_text='1: Windows, 2: iOS, 3: Android, 4: browser, 5: others'
    )

    link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Link'

    def __str__(self):
        return self.get_type_display()


class Development(models.Model):  # ゲーム情報テーブル
    id = models.BigAutoField(primary_key=True, editable=False)

    title = models.CharField(max_length=30)
    description = models.TextField()

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.PROTECT, related_name='development_user')
    # 共同開発者
    users = models.ManyToManyField(User, related_name='development_users')

    associations = models.ManyToManyField(
        Association,
        related_name='development_associations',
        blank=True
    )

    status = models.IntegerField(
        _('status'),
        help_text='0: 申請中, 1: 公開中, 2: 非公開',
        default=0,
    )

    # みす限定公開か否か
    is_private = models.BooleanField(
        default=False,
        help_text='Open only within misw or not'
    )

    top_image = models.ImageField(
        _('top_image'),
        upload_to='images/Development',
        help_text='top image to be listed to home',
        blank=True,
        null=True
    )

    medias = models.ManyToManyField(Media, _('Medias'))

    links = models.ManyToManyField(Link, _('links'))

    # times
    submitted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Development'

    def __str__(self):
        return self.title
