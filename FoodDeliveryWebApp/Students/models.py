from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    studentID = models.CharField(max_length=8)
    studentName = models.CharField(max_length=100)
    hostelID = models.ForeignKey(User, on_delete=models.CASCADE)
    accountNumber = models.CharField(max_length=10)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=50)