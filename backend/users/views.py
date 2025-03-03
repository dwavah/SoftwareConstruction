from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    querryset = CustomUser.objects.all()
    serializer_class = UserSerializer

