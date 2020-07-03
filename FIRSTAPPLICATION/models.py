from django.db import models

# Create your models here.


class Employee(models.Model):
    FirstName = models.CharField(max_length=50)
    EmpID = models.CharField(max_length=50)
    Contact = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
