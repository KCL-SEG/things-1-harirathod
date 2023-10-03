from django.db import models
from django.db.models import Model
# Create your models here.

class Thing(Model):
    name = models.CharField(
        verbose_name="name", 
        unique=False, 
        max_length=30)
    
    description = models.CharField(
        verbose_name='description', 
        unique=False, 
        max_length=120)
    
    quantity = models.IntegerField(
        verbose_name='quantity')