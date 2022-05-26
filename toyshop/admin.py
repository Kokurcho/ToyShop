# type: ignore
from django.contrib import admin
from .models import Toy, Manufacturer

# Register your models here.


class ToyInline(admin.StackedInline):
    model = Toy
    
    
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    inlines: [ToyInline]


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ('name','material','manufacturer')


#admin.site.register(Toy)
#admin.site.register(Manufacturer)



