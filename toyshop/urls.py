# type: ignore
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("manufacturers/", views.ManufacturerListView.as_view()),
    path("manufacturers/<int:pk>/", views.ManufacturerDetailView.as_view()),
    path("toys/", views.ToyListView.as_view()),
    path("toys/<int:pk>/", views.ToyDetailView.as_view()),
    path("add_manufacturer/", views.ManufacturerCreateView.as_view()),
    path("add_toy/", views.ToyCreateView.as_view()),
]