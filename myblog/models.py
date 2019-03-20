from django.db import models

# Create your models here.
class article(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=200)
    assortment = models.CharField(max_length=50)
    visitors = models.IntegerField()
    pubDate = models.DateField()
    modifyDate = models.DateField()
    content = models.TextField()
    img = models.ImageField(default=False)
    alt = models.CharField(max_length=100)
    summary = models.TextField()
    pubTag = models.BooleanField(default=False)