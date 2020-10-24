from django.db import models

# Create your models here.
def gameInf(models.Model):
    gameid = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    userid = models.IntegerField()
    status = models.IntegerField()
    image = models.ImageField(upload_to='images/gameInf')
    submittedtime = models.DateTimeField()
    updatedtime = models.DateTimeField()

def gameScore(models.Model):
    gameid = models.IntegerField()
    player = models.TextField()
    score = models.IntegerField()