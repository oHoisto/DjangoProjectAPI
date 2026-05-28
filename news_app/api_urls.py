from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .viewsets import UserViewSet, NewsViewSet


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('news', NewsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api_token'),
]