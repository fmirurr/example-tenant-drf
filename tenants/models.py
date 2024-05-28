from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    database_name = models.CharField(max_length=100, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name