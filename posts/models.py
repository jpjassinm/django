from django.db import models

# Create your models here.
class persona(models.model):
    
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_leng=100)
    fist_names=models.CharField(max_leng=100)
    last_name=models.CharField(max_leng=100)
    bio = models.TextField(max_leng=100)
    birthdate=models.DateField()
    created=models.DateField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)