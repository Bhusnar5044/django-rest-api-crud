from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)