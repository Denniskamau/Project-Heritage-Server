from django.db import models

# Create your models here.
class Attendance(models.Model):
    isPresent = models.BooleanField()
    childName = models.CharField(max_length=30)
    