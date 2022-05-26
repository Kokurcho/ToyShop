# type: ignore
from importlib.resources import path
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ToysView.as_view()),    
    re_path(r'^main_menu', views.main_menu),
]