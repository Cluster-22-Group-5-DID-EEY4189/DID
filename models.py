from django.db import models

# Create your models here.
# identification/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

