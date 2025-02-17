from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include(router.urls)),
]