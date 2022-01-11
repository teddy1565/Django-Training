from django.db import models

# Create your models here.

class USER(models.Model):
    usr = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    def __str__(self):
        return self.usr