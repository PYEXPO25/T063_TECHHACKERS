from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
    
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_type = models.CharField(max_length=30)
    complaint_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Complaint by {self.user.username}"
    
class Admin(models.Model):
    username = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 225)

    def __str__(self):
        return self.username

    
