from django.db import models

# Create your models here.

class FilePathModel(models.Model):
    path = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    displaySetting = models.IntegerField()

class FileNameModel(models.Model):
    path = models.CharField(max_length=1000)
    fileName = models.CharField(max_length=100)
    displaySetting = models.IntegerField()