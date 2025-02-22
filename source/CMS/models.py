from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
    
class Admin(models.Model):
    username = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 225)

    def __str__(self):
        return self.username
    
class PersonalInfo(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()

    def __str__(self):
        return self.full_name

class PersonalInfo(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # Increased max_length for flexibility
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()

    def __str__(self):
        return self.full_name

class Complaints(models.Model):
    CATEGORY_CHOICES = [
        ('water', 'Water Issue'),
        ('electric', 'Electric Issue'),
        ('garbage', 'Garbage'),
        ('toilet', 'Toilet Maintenance'),
        ('lake', 'Lake Work'),
        ('park', 'Park Maintenance'),
        ('road', 'Speed Breaker'),
        ('drainage', 'Drainage'),
        ('other', 'Other'),
    ]

    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="complaints")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=2000)
    location = models.CharField(max_length=255, blank=True, null=True)
    attachment = models.FileField(upload_to='complaints/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.personal_info.full_name} - {self.category}"
    
