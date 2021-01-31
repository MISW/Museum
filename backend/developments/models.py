from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_comma_separated_integer_list

from backend.users.models import User

MEDIA_CHOICES = (
    (0, '画像'),
    (1, '音声'),
    (2, '動画')
)

LINK_CHOICES = (
    (0, 'Windows'),
    (1, 'iOS'),
    (2, 'Android'),
    (3, 'ブラウザ'),
    (4, 'その他')
)

ASSOCIATION_CHOICES = (
    (0, 'プログラミング'),
    (1, 'CG'),
    (2, 'MIDI')
)

STATUS_CHOICES = (
    (0, '申請中'),
    (1, '公開中'),
    (2, '非公開')
)

class Media(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)

    type = models.IntegerField(
        choices=MEDIA_CHOICES,
        help_text='0: image, 1: sound, 2: video'
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
        help_text='0: Windows, 1: iOS, 2: Android, 3: browser, 4: others'
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

    user = models.ForeignKey(
        User,
        verbose_name='User',
        on_delete=models.PROTECT,
        related_name='development_user'
    )
    # 共同開発者
    users = models.ManyToManyField(User, related_name='development_users', blank=True)

    associations = models.CharField(
        _('associations'),
        validators=[validate_comma_separated_integer_list],
        max_length=6,
        help_text='0: programming, 1: CG, 2: MIDI',
        blank=True,
        null=True,
        default=''
    )

    status = models.IntegerField(
        _('status'),
        choices=STATUS_CHOICES,
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
        upload_to='images/development',
        help_text='top image to be listed to home',
        blank=True,
        null=True
    )

    medias = models.ManyToManyField(Media, _('Medias'), blank=True)

    links = models.ManyToManyField(Link, _('links'), blank=True)

    # times
    submitted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Development'

    def __str__(self):
        return self.title

    def get_associations(self) -> list:
        associations = self.associations
        if not associations:
            return []
        return associations.split(',')

    def get_associations_display(self) -> str:
        return ', '.join(
            [ASSOCIATION_CHOICES[int(data)][1] for data in self.get_associations()]
        )



