from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('admin', 'ADMIN'),
        ('author', 'AUTHOR'),
        ('reader', 'READER'),
    )
    
    
    role = models.CharField(
        max_length = 20,
        choices= ROLE_CHOICES,
        default= 'reader'
    )
    
    
    def __str__(self):
        return self.username
