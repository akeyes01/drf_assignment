from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

router = DefaultRouter()
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    #path('api/', include(router.urls)),
]