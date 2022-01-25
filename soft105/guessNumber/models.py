from django.db import models

# Create your models here.

class GuessNumberModel(models.Model):
    num = models.IntegerField()