from django.db import models

# Create your models here.

class PWD(models.Model):
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.password