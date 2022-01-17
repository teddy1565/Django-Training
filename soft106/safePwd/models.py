from django.db import models

# Create your models here.

class PWD(models.Model):
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.account}\t{self.password}"