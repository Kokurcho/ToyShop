# type: ignore

from unicodedata import category
from rest_framework import serializers
from .models import Manufacturer, Toy

# GET
class ManufacturerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ("name", "address")


class ManufacturerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ("name", "address")


class ToyListSerializer(serializers.ModelSerializer):
    manufacturer = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Toy
        fields = ("name", "material","manufacturer")


class ToyDetailSerializer(serializers.ModelSerializer):
    manufacturer = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Toy
        fields = ("name", "material","manufacturer")

#POST
class ManufacturerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"

class ToyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = "__all__"
