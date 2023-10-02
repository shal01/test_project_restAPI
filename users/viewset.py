from django.contrib.auth.models import User

from rest_framework import viewsets,mixins
from .permissions import IsUserOwnerOrGetAndPostOnly,IsProfileOwnerGetAndPostOnly
from users.serializer import UserSerializer,ProfileSerializers
from .models import Profile

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin, mixins.UpdateModelMixin , mixins.ListModelMixin):
    permission_classes = [IsProfileOwnerGetAndPostOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers





