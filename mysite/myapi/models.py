from django.db import models
from django.contrib.auth.models import User


class House(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True, null=True)
    changes_date = models.DateField(auto_now=True, null=True)
    photo = models.FilePathField(path='/', null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True, null = True)
    changes_date = models.DateField(auto_now=True, null = True)
    photo = models.FilePathField(path='/', null=True)
    house = models.ForeignKey(House, on_delete = models.CASCADE)

    def __str__(self):
        return self.name.title()


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True,null = True)
    changes_date = models.DateField(auto_now=True,null = True)
    photo = models.FilePathField(path='/', null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.title()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name.title()


class Object(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True, null=True)
    changes_date = models.DateField(auto_now=True, null=True)
    photo = models.FilePathField(path='/', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, through='ObjectCategory')

    def __str__(self):
        return self.name()


class ObjectCategory(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
