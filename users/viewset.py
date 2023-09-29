from django.contrib.auth.models import User

from rest_framework import viewsets
from .permissions import IsUserOwnerOrGetAndPostOnly
from users.serializer import UserSerializer,ProfileSerializers
from .models import Profile

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers





