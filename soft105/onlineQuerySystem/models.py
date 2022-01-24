from django.db import models

# Create your models here.

class Users(models.Model):
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Question(models.Model):
    account = models.CharField(max_length=100)
    inputText = models.TextField(blank=True)