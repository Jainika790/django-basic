from django.db import models

# Create your models here.

class Login_User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_no=models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
