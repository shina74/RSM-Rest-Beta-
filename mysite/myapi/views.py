from rest_framework import viewsets
from .serializers import HouseSerializer, RoomSerializer, PlaceSerializer, ObjectSerializer, CategorySerializer
from .models import House, Room, Place, Object, Category


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all().order_by('name')
    serializer_class = HouseSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('name')
    serializer_class = RoomSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by('name')
    serializer_class = PlaceSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all().order_by('name')
    serializer_class = ObjectSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

