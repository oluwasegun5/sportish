from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'auth_app'

router = SimpleRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]