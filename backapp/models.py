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
>>>>>>> 66ff872411afaa13ba2c803fed931704e179b402
