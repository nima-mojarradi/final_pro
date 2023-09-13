from django.db import models

class ModelParser(models.Model):
    link = models.URLField(null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField(null=True,blank=True)
