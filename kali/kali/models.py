from django.db import models
from django.contrib.auth.models import User
import os
from .settings import BASE_DIR

class Art(models.Model):
    name = models.CharField(max_length=512, blank=False)
    preview = models.TextField(blank=True)
    likes = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(blank=False, default=os.path.join(BASE_DIR, '/static/main/img/404.jpg'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class ArtComment(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    art     = models.ForeignKey(Art, on_delete=models.CASCADE)
    text    = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Comission(models.Model):
    name = models.CharField(max_length=512, blank=False)
    price = models.IntegerField(blank=False)
    preview = models.TextField(blank=True)
    likes = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(blank=False, default=os.path.join(BASE_DIR, '/static/main/img/404.jpg'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_author")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class ComissionComment(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    comission    = models.ForeignKey(Comission, on_delete=models.CASCADE)
    text    = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class UserSettings(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    color_theme = models.BooleanField(null=True)
    no_ai_tag = models.BooleanField(null=True)
    display_name = models.CharField(max_length=100, null=False)
    bio = models.TextField(blank=True)
    timezone = models.SmallIntegerField(default=3)
    

    def __str__(self):  
          return "%s's settings" % self.user 
    
class Tag(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    
class ArtTag(models.Model):
    art_id = models.OneToOneField(Art, on_delete=models.CASCADE)  
    tag_id = models.OneToOneField(Tag, on_delete=models.CASCADE)  

class ComissionTag(models.Model):
    comission_id = models.OneToOneField(Comission, on_delete=models.CASCADE)  
    tag_id = models.OneToOneField(Tag, on_delete=models.CASCADE)  

class Order(models.Model):
    title = models.CharField(blank=False)
    price = models.FloatField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created = models.DateField(blank=False)
