from django.db import models

# Create your models here.
class PhClass(models.Model):
    ageGroup =models.CharField(max_length= 30)
    class_designation = models.CharField(max_length =64,default='CLASS A')
    name = models.CharField(max_length=64,default='N/A')
    min_age = models.IntegerField(default=3)
    max_age = models.IntegerField(default=6)


