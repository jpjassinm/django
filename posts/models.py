from django.db import models

# Create your models here.
class Persona(models.Model):
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    fist_names = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)