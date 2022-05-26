# type: ignore
from django.shortcuts import render
from django.views.generic.base import View
from .models import Toy
from .models import Manufacturer

# Create your views here.

class ToysView (View):
    def get(self, request):
        toys = Toy.objects.all()
        return render(request, "toys/toy_list.html", {"toy_list" : toys})


def main_menu(request):
    return render(request, "main_menu.html")