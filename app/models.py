from django.db import models

# Create your models here.
class UserReg(models.Model):
    email=models.EmailField(max_length=200,unique=True,blank=False)
    password=models.CharField(max_length=300)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20,unique=True,blank=False)
    user_id=models.CharField(max_length=50,unique=True,blank=False)
    role=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name} ({self.email})"