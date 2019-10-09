from django.db import models
from classes.models import PhClass
# Create your models here.
class Attendance(models.Model):
    phClass = models.ForeignKey(PhClass,on_delete=models.CASCADE)
    isPresent = models.BooleanField(default=False)
    childName = models.CharField(max_length=30)

