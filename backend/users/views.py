from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from .models import CustomUser
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPView):
    querryset = CustomUser.objects.all()
    serializer_class = UserSerializer

