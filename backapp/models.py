<<<<<<< HEAD
from django.db import models

# Create your models here.
class gameInf(models.Model): #ゲーム情報テーブル
    gameid = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    userid = models.IntegerField()
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
    developerid = models.IntegerField()
    partinf = models.TextField()

class developerInf(models.Model): #開発者情報テーブル
    developerid = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/developerInf')

class developPartInf(models.Model): #開発者マスタ
    developerid = models.IntegerField()
    developername = models.TextField()
    generation = models.IntegerField()

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
=======
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
    submittedtime = models.DateTimeField(blank=True, null=True)
    updatedtime = models.DateTimeField(blank=True, null=True)
    link_browser = models.TextField(blank=True, null=True)
    link_Windows = models.TextField(blank=True, null=True)
    link_Mac = models.TextField(blank=True, null=True)
    link_Android = models.TextField(blank=True, null=True)
    link_iOS = models.TextField(blank=True, null=True)

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

<<<<<<< HEAD
class categoryInf(models.Model): #カテゴリマスタ
    categoryid = models.IntegerField()
    categoryname = models.TextField()
>>>>>>> 66ff872411afaa13ba2c803fed931704e179b402
=======
    def __str__(self):
        return self.title
>>>>>>> bd3ef387cd4e82b22e2d08c12ea1b4e585302fa7
