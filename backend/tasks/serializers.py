from rest_framework import serializers
from .models import Task  # Ensure this matches your actual model name

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '_all_'  # Or specify the fields you need