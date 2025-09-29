from django.db import models

# Create your models here.
class UserReg(models.Model):
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    user_id=models.CharField(max_length=50)
    role=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.devotee_name} ({self.phone_number})"