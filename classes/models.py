from django.db import models

"""
Admin(facilitator | curiculum developers | IT Support | child) APP
user-types


TASK
    - Facilitator (id)
    - minAge = models.IntegerField()
    - maxAge = models.IntegerField()
"""

# Create your models here.
class PhClass(models.Model):
    # enumration

    ageGroup =models.CharField(max_length= 30)
    facilitator = models.CharField(max_length=200,blank=True)

# class Facilitators(models.Model):
#     firstname = models.CharField(max_length=64)
#     lastname = models.CharField(max_length=64)
