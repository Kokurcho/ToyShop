# type: ignore
from .models import Toy, Manufacturer
from .serializers import ManufacturerListSerializer, ManufacturerDetailSerializer, ToyListSerializer, ToyDetailSerializer
from .serializers import ManufacturerCreateSerializer, ToyCreateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

#GET

class ManufacturerListView(APIView):
    def get(self, request):
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerListSerializer(manufacturers, many=True)
        return Response(serializer.data)


class ManufacturerDetailView(APIView):
    def get(self, request, pk):
        manufacturer = Manufacturer.objects.get(id=pk)
        serializer = ManufacturerDetailSerializer(manufacturer)
        return Response(serializer.data)


class ToyListView(APIView):
    def get(self, request):
        toys = Toy.objects.all()
        serializer = ToyListSerializer(toys, many=True)
        return Response(serializer.data)


class ToyDetailView(APIView):
    def get(self, request, pk):
        toy = Toy.objects.get(id=pk)
        serializer = ToyListSerializer(toy)
        return Response(serializer.data)

#POST

class ManufacturerCreateView(APIView):
    def post(self, request):
        manufacturer = ManufacturerCreateSerializer(data = request.data)
        if manufacturer.is_valid():
            manufacturer.save()
        return Response(status=201)


class ToyCreateView(APIView):
    def post(self, request):
        toy = ToyCreateSerializer(data = request.data)
        if toy.is_valid():
            toy.save()
        return Response(status=201)