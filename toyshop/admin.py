# type: ignore
from django.contrib import admin
from .models import Toy, Manufacturer

# Register your models here.

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name','address')


class ManufacturerInline(admin.TabularInline):
    model = Manufacturer


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ('name','material','manufacturer')
    inlines: [ManufacturerInline]
