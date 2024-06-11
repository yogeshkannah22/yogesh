from django.db import models

# Create your models here.

class data(models.Model):
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    clgName=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    email=models.EmailField()
