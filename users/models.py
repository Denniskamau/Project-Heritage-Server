from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
# from classes.models import PhClass
# Create your models here.


class User(AbstractUser):
    is_parent=models.BooleanField(default=False)
    is_child = models.BooleanField(default=True)
    is_facilitator = models.BooleanField(default=False)

class Parent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    pri_phone_no = models.CharField(max_length=64,null=True)
    sec_phone_no = models.CharField(max_length=64,null=True)
    neighbourhood = models.CharField(max_length=64,null=True)


class Child(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    age = models.IntegerField(default=3)
    dob = models.DateTimeField(default=datetime.datetime.now)
    is_active = models.BooleanField(default=False)
    # attendace = models.ForeignKey('attendance.Attendance',default=1,on_delete=models.CASCADE)
    phclass = models.ForeignKey('classes.PhClass',default=1,on_delete=models.CASCADE)
    progresreport= models.ForeignKey('ProgressReport',on_delete=models.CASCADE,null=True)
    # ph_class_id = models.ForeignKey('classes.PhClass',on_delete=models.CASCADE)

class Facilitator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    phclass = models.ManyToManyField('classes.PhClass')

class Parent_Child(models.Model):
    parent_id = models.ForeignKey(Parent,on_delete=models.CASCADE)
    child_id = models.ForeignKey(Child,on_delete=models.CASCADE)

class ProgressReport(models.Model):
    notes = models.TextField();
    child_id = models.ForeignKey(Child,on_delete=models.CASCADE)
    facilitator = models.ManyToManyField('Facilitator')

class ChildDetails(models.Model):
    school = models.CharField(max_length=64)
    stage = models.CharField(max_length=64)
    special_needs = models.TextField()
    child = models.OneToOneField('Child',on_delete=models.CASCADE)