from django.db import models
from django.urls import reverse

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 120)
    pricee = models.DecimalField(max_digits = 120, decimal_places=2)
    summarry = models.TextField(blank = True, null=False)
    featured = models.BooleanField(default=  False)

    def get_absolute_url(self):
        return reverse("package:package_view")