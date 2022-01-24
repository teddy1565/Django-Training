from django.db import models

# Create your models here.

class Users(models.Model):
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.password

class Question(models.Model):
    acccount = models.CharField(max_length=100)
    inputText = models.TextField()
    def __str__(self):
        return self.inputText