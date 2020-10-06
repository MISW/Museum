from django.db import models

from accounts.models import CustomUser

# Create your models here.
class GameInf(models.Model): #ゲーム情報テーブル
    gameid = models.IntegerField(blank=True, null=True)
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    status = models.IntegerField()
    image = models.ImageField(upload_to='images/GameInf')
    submittedtime = models.DateTimeField()
    updatedtime = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'GameInf'
    
    def __str__(self):
        return self.title

class GameScore(models.Model): #ゲームスコアテーブル
    gameid = models.IntegerField(blank=True, null=True)
    player = models.TextField()
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'GameScore'
    
    def __str__(self):
        return self.title

class DevelopPartInf(models.Model): #ゲーム開発者テーブル
    gameid = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    partinf = models.TextField()

    class Meta:
        verbose_name_plural = 'DevelopPartInf'
    
    def __str__(self):
        return self.title

class DeveloperInf(models.Model): #開発者情報テーブル
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'DeveloperInf'
    
    def __str__(self):
        return self.title

class StatusInf(models.Model): #状態マスタ
    statusid = models.IntegerField(blank=True, null=True)
    statusname = models.TextField()

    class Meta:
        verbose_name_plural = 'StatusInf'
    
    def __str__(self):
        return self.title

class DownloadLinkInf(models.Model): #ダウンロードリンクテーブル
    gameid = models.IntegerField(blank=True, null=True)
    machineid = models.IntegerField(blank=True, null=True)
    link = models.TextField()

    class Meta:
        verbose_name_plural = 'DownloadLinkInf'
    
    def __str__(self):
        return self.title

class MachineInf(models.Model): #機種マスタ
    machineid = models.IntegerField(blank=True, null=True)
    machinename = models.TextField()

    class Meta:
        verbose_name_plural = 'MachineInf'
    
    def __str__(self):
        return self.title

class GameCategoryInf(models.Model): #カテゴリテーブル
    gameid = models.IntegerField(blank=True, null=True)
    categoryid = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'GameCategoryInf'
    
    def __str__(self):
        return self.title

class CategoryInf(models.Model): #カテゴリマスタ
    categoryid = models.IntegerField(blank=True, null=True)
    categoryname = models.TextField()

    class Meta:
        verbose_name_plural = 'CategoryInf'
    
    def __str__(self):
        return self.title