from django.db import models


class Bicycle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)
    type = models.CharField(max_length=255)
    handlebar = models.CharField(max_length=255)
    marches = models.IntegerField(default=0)
    material = models.CharField(max_length=255)
    cube = models.CharField(max_length=255)
    rear_cube = models.CharField(max_length=255)
    tires = models.CharField(max_length=255)

    def __str__(self):
        return self.name
