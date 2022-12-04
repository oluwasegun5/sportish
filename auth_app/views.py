from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from auth_app.models import User
from auth_app.serializers import UserCreateSerializer, UserSerializer


# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['username', 'first_name', 'last_name', 'email']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer
