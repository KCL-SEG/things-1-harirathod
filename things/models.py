from django.db import models
from django.db.models import Model
import django.core.validators 
# Create your models here.

class Thing(Model):
    name = models.CharField(
        verbose_name="name", 
        unique=True, 
        max_length=30,
        blank=False)
    
    description = models.CharField(
        verbose_name='description', 
        unique=False,
        max_length=120,
        blank=True)
    
    quantity = models.IntegerField(
        verbose_name='quantity',
        unique=False,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(100),
        ],
        )