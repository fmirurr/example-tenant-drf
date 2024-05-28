from django.db import models

# Create your models here.
class SomeModel(models.Model):
    _database = 'tenant'
    name = models.CharField(max_length=244)