from django.db import models

# Create your models here.

class Card(models.Model):
    uid = models.CharField(max_length=100)
    def __str__(self):
        return self.uid