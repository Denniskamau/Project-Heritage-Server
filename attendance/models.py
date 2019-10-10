from django.db import models
from classes.models import PhClass
# Create your models here.
class Attendance(models.Model):
    isPresent = models.BooleanField(default=False)

