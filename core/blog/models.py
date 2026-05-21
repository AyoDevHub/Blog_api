from django.db import models
from django.contrib.auth.models import User 


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
        )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


