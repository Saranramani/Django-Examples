from django.db import models

class Todos(models.Model):
    todo = models.CharField(max_length=100)
    