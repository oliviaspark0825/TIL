from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)  
    email = models.CharField(max_length=100)
    birthday = models.DateTimeField(auto_now_add=True) 
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}:{self.name}"
