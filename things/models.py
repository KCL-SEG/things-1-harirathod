from django.db import models
from django.db.models import Model
# Create your models here.

class Thing(Model):
    name = models.CharField(
        verbose_name="name")
    
    description = models.CharField(
        verbose_name='description')
    
    quantity = models.IntegerField(
        verbose_name='quantity')