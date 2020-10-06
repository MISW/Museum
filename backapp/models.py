from django.db import models

from accounts.models import CustomUser

# Create your models here.
class gameInf(models.Model): #ゲーム情報テーブル
    gameid = models.IntegerField(blank=True, null=True)
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    status = models.IntegerField()
    image = models.ImageField(upload_to='images/gameInf')
    submittedtime = models.DateTimeField()
    updatedtime = models.DateTimeField()

class gameScore(models.Model): #ゲームスコアテーブル
    gameid = models.IntegerField(blank=True, null=True)
    player = models.TextField()
    score = models.IntegerField(blank=True, null=True)

class developPartInf(models.Model): #ゲーム開発者テーブル
    gameid = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    partinf = models.TextField()

class developerInf(models.Model): #開発者情報テーブル
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    description = models.TextField()

class statusInf(models.Model): #状態マスタ
    statusid = models.IntegerField(blank=True, null=True)
    statusname = models.TextField()

class downloadLinkInf(models.Model): #ダウンロードリンクテーブル
    gameid = models.IntegerField(blank=True, null=True)
    machineid = models.IntegerField(blank=True, null=True)
    link = models.TextField()

class machineInf(models.Model): #機種マスタ
    machineid = models.IntegerField(blank=True, null=True)
    machinename = models.TextField()

class GameCategoryInf(models.Model): #カテゴリテーブル
    gameid = models.IntegerField(blank=True, null=True)
    categoryid = models.IntegerField(blank=True, null=True)

class categoryInf(models.Model): #カテゴリマスタ
    categoryid = models.IntegerField(blank=True, null=True)
    categoryname = models.TextField()