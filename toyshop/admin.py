# type: ignore
from django.contrib import admin
from .models import Toy, Manufacturer

# Register your models here.


# @admin.register(Toy)
# class ToyAdmin(admin.ModelAdmin):
#     list_display = ('name','material','manufacturer')


# class ToyInline(admin.TabularInline):
#     model = Toy

    
# @admin.register(Manufacturer)
# class ManufacturerAdmin(admin.ModelAdmin):
#     list_display = ('name','address')
#     inlines: [ToyInline]



#admin.site.register(Toy)
#admin.site.register(Manufacturer)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name','address')


class ManufacturerInline(admin.TabularInline):
    model = Manufacturer


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ('name','material','manufacturer')
    inlines: [ManufacturerInline]
