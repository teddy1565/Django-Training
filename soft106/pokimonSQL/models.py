from django.db import models

# Create your models here.

class Pokemon(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    pokemonType=models.CharField(max_length=100)
    serial = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 0