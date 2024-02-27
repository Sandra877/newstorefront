from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length = 120)
    details = models.CharField(max_length = 200)
    blogs = models.TextField(max_length = 10000)
