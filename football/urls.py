from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'football'

router = SimpleRouter()
router.register('teams', views.TeamViewSet)
router.register('players', views.PlayerViewSet)
router.register('managers', views.ManagerViewSet)
router.register('hosts', views.HostViewSet)
router.register('competitions', views.CompetitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
