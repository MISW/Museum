from django.db import models
from django.db.models.fields import BigAutoField
from django.utils.translation import gettext_lazy as _

from backend.users.models import User
from backend.users.models import Association


LINK_CHOICES = (
    (1, '画像'),
    (2, '音声'),
    (3, '動画'),
    ('URL', (
            (41, 'Windows'),
            (42, 'iOS'),
            (43, 'Android'),
            (44, 'browser'),
            (45, 'others')
        )
    )

)

class LinkInf(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)

    type = models.IntegerField(
        choices=LINK_CHOICES,
        help_text=('1: image, 2: sound, 3: video, 4: URLS(41: Windows, 42: iOS, 43: Android, 44: browser, 45: others)')
    )

    link = models.URLField(blank=True, null=True)

    file = models.FileField(
        upload_to='files/DeveloperInf',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = 'LinkInf'
    
    def __str__(self):
        return self.get_type_display()


class DevelopmentInf(models.Model): #ゲーム情報テーブル
    id = models.BigAutoField(primary_key=True, editable=False)

    title = models.TextField()
    description = models.TextField()

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.PROTECT, related_name='developmentinf_user')
    # 共同開発者
    users = models.ManyToManyField(User, related_name='developmentinf_users')

    associations = models.ManyToManyField(
        Association,
        related_name='developmentinf_associations',
    )

    status = models.IntegerField(
        _('status'),
        help_text=('0: 申請中, 1: 公開中, 2: 非公開'),
        default=0,
    )
    
    # みす限定公開か否か
    is_public = models.BooleanField(
        default=False,
        help_text=('Open only within misw or not')
    )

    top_image = models.ImageField(
        _('top_image'),
        upload_to='images/DevelopmentInf',
        help_text=('top image to be listed to home'),
        blank=True,
        null=True
    )

    links = models.ManyToManyField(
        LinkInf,
        _('links'),
        blank=True
    )

    # times
    submitted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'DevelopmentInf'

    def __str__(self):
        return self.title


