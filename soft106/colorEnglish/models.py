from django.db import models

# Create your models here.

class GameModel(models.Model):
    uid = models.CharField(max_length=100)
    def __str__(self):
        return self.uid

class GameContentModel(models.Model):
    pass
    def __str__(self):
        return 0
