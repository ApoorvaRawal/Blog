from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    Categories=models.ManyToManyField(Category)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    
        
            
