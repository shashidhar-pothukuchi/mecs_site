from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    gender=models.CharField(max_length=10)
    RollNo=models.CharField(max_length=200)
    branch=models.CharField(max_length=5)
    
    def __str__(self):
        return self.RollNo