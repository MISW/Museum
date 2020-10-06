from django.db import models

from accounts.models import CustomUser

# Create your models here.
"""
class gameInf(models.Model): #ゲーム情報テーブル
    gameid = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    status = models.IntegerField()
    image = models.ImageField(upload_to='images/gameInf')
    submittedtime = models.DateTimeField()
    updatedtime = models.DateTimeField()

class gameScore(models.Model): #ゲームスコアテーブル
    gameid = models.IntegerField()
    player = models.TextField()
    score = models.IntegerField()

class developPartInf(models.Model): #ゲーム開発者テーブル
    gameid = models.IntegerField()
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    partinf = models.TextField()

class developerInf(models.Model): #開発者情報テーブル
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    description = models.TextField()

class developPartInf(models.Model): #開発者マスタ
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)

class statusInf(models.Model): #状態マスタ
    statusid = models.IntegerField()
    statusname = models.TextField()

class downloadLinkInf(models.Model): #ダウンロードリンクテーブル
    gameid = models.IntegerField()
    machineid = models.IntegerField()
    link = models.TextField()

class machineInf(models.Model): #機種マスタ
    machineid = models.IntegerField()
    machinename = models.TextField()

class GameCategoryInf(models.Model): #カテゴリテーブル
    gameid = models.IntegerField()
    categoryid = models.IntegerField()

class categoryInf(models.Model): #カテゴリマスタ
    categoryid = models.IntegerField()
    categoryname = models.TextField()
"""