from django.db import models
from user.models import CustomUser
class ModelParser(models.Model):
    link = models.URLField(null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    itunes_author = models.CharField(max_length=100, default='Unknown', null=True, blank=True)
    itunes_duration = models.CharField(max_length=100, null=True, blank=True)
    images=models.TextField(default='image url')

    def __str__(self) -> str:
        return self.title


class Like(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='user')
    podcast = models.OneToOneField(ModelParser, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    context = models.TextField()
    podcast = models.OneToOneField(ModelParser, on_delete=models.CASCADE)
    
