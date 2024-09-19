# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Consider hashing passwords for security

    def __str__(self):
        return self.name
