from rest_framework import serializers
from .models import House, Room, Place, Object, Category


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'name', 'description', 'creation_date', 'changes_date', 'photo')


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'description', 'creation_date', 'changes_date', 'photo', 'house')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'description', 'creation_date', 'changes_date', 'photo', 'room')


class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = ('name', 'description', 'creation_date', 'changes_date', 'photo', 'place', 'category')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
