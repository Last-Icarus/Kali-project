from django.db import models
from django.contrib.auth.models import User
import os
from .settings import BASE_DIR

class Art(models.Model):
    name = models.CharField(max_length=512, blank=False, null=False)
    preview = models.TextField(blank=True)
    likes = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(blank=False, default=os.path.join(BASE_DIR, '/static/main/img/404.jpg'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name

class ArtComment(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    art     = models.ForeignKey(Art, on_delete=models.CASCADE)
    text    = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Commission(models.Model):
    name = models.CharField(max_length=512, blank=False, null=False)
    price = models.FloatField(blank=False)
    preview = models.TextField(blank=True)
    likes = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(blank=False, default=os.path.join(BASE_DIR, '/static/main/img/404.jpg'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_author")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class CommissionComment(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    Commission    = models.ForeignKey(Commission, on_delete=models.CASCADE)
    text    = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class UserSettings(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)  
    no_ai_tag = models.BooleanField(null=True, blank=False, default=False)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    header = models.ImageField(upload_to='headers/', blank=True)

    def __str__(self):  
          return "%s's settings" % self.user 
    
class Tag(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    
class ArtTag(models.Model):
    art_id = models.OneToOneField(Art, on_delete=models.CASCADE, blank=False, null=False)  
    tag_id = models.OneToOneField(Tag, on_delete=models.CASCADE, blank=False, null=False)  

class CommissionTag(models.Model):
    Commission_id = models.OneToOneField(Commission, on_delete=models.CASCADE, blank=False, null=False)  
    tag_id = models.OneToOneField(Tag, on_delete=models.CASCADE, blank=False, null=False)  

class Order(models.Model):
    title = models.CharField(blank=False, max_length=128)
    price = models.FloatField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created = models.DateField(blank=False)

class ArtImage(models.Model):
    art = models.OneToOneField(Art, on_delete=models.CASCADE, blank=False,null=False)
    image = models.ImageField(blank=False, null=False)


class CommissionImage(models.Model):
    commission = models.OneToOneField(Commission, on_delete=models.CASCADE, blank=False,null=False)
    image = models.ImageField(blank=False, default=os.path.join(BASE_DIR, '/static/main/img/404.jpg'))
