from django.db import models

# Create your models here.
class PhClass(models.Model):
    age_group =models.CharField(max_length= 30)
    facilitator = models.CharField(max_length=200,blank=True)

