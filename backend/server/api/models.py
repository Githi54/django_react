from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    id = models.UUIDField(auto_created=True, max_length=10, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Good(models.Model):
    category_id = models.UUIDField(auto_created=True, max_length=10)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(validators=[MaxValueValidator(1000), MinValueValidator(10)])
    
    def __str__(self):
        return self.name