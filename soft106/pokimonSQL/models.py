from django.db import models

# Create your models here.

class Pokemon(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    pokemonType=models.CharField(max_length=100)
    serial = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        result = f"<pre>{self.uid}\t{self.name}\t{self.position}\t{self.pokemonType}\t{self.serial}\t{self.date}</pre>"
        return result