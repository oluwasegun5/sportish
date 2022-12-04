from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import *


class PlayerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Player.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['strong_foot', 'user__username', 'user__first_name', 'user__last_name', 'user__email',
                     'team__teamName', 'height']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PlayerCreateSerializer
        return PlayerSerializer


class HostViewSet(ModelViewSet):
    queryset = Host.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HostCreateSerializer
        return HostSerializer


class CompetitionViewSet(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompetitionCreateSerializer
        return CompetitionSerializer


class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.select_related('user').all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ManagerCreateSerializer
        return ManagerSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TeamCreateSerializer
        return TeamSerializer
