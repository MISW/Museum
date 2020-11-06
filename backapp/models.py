from django.db import models

from accounts.models import CustomUser

# Create your models here.
class GameInf(models.Model): #ゲーム情報テーブル
    # (primary key)
    gameid = models.IntegerField(blank=True, null=True)

    title = models.TextField()
    description = models.TextField()

    # Foreign key
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    # 0: 申請中
    # 1: 公開中
    # 2: 非公開
    status = models.IntegerField()
    # game image
    image = models.ImageField(upload_to='images/GameInf',blank=True, null=True)
    # times
    submittedtime = models.DateTimeField(blank=True, null=True)
    updatedtime = models.DateTimeField(blank=True, null=True)

    # machine links
    link_browser = models.TextField(blank=True, null=True)
    link_Windows = models.TextField(blank=True, null=True)
    link_Mac = models.TextField(blank=True, null=True)
    link_Android = models.TextField(blank=True, null=True)
    link_iOS = models.TextField(blank=True, null=True)

    # category info
    categoryid = models.IntegerField(blank=True, null=True)
    categoryname = models.TextField(blank=True, null=True)


    class Meta:
        verbose_name_plural = 'GameInf'

    def __str__(self):
        return self.title


class DeveloperInf(models.Model): #開発者情報テーブル
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'DeveloperInf'

    def __str__(self):
        return self.user.username

# 保留 ==========================================================================================

class GameScore(models.Model): #ゲームスコアテーブル
    gameid = models.IntegerField(blank=True, null=True)
    player = models.TextField()
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'GameScore'

    def __str__(self):
        return '{}_{}'.format(self.gameid, self.player)

class DevelopPartInf(models.Model): #ゲーム開発者テーブル
    gameid = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    partinf = models.TextField()

    class Meta:
        verbose_name_plural = 'DevelopPartInf'

    def __str__(self):
        return self.user
