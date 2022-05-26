# type: ignore
from django.contrib import admin
from .models import Toy, Manufacturer

# Register your models here.

admin.site.register(Toy)
admin.site.register(Manufacturer)