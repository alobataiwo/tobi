from django.db import models

# Create your models here.

class Modal(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email_address=models.EmailField(max_length=254)
