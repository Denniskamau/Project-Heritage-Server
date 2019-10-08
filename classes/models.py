from django.db import models

# Create your models here.
class PhClass(models.Model):
    age_group =models.CharField()
    facilitator = models.CharField(blank=True)

    