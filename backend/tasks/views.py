from django.shortcuts import render
from rest_framework import Task
from .serializers import TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    querryset = Task.objects.all()
    serializer_class = TaskSerializer