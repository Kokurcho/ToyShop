# type: ignore
from django.db import models

# Create your models here.
class Manufacturer (models.Model):
    name = models.CharField ("Name", max_length=150)
    address = models.CharField ("Address", max_length=150)

    def __str__(self):
        return self.name

class Toy (models.Model):
    name = models.CharField ("Name", max_length=150)
    material = models.CharField ("Material", max_length=150)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="toys")

    def __str__(self):
        return self.name 

