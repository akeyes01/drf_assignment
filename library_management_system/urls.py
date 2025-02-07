"""
URL configuration for library_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lms_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # New code
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('auths/', views.authordata),
    path('books/', views.bookdata),
    path('loans/', views.loandata),
    path('members/', views.memberdata),
    path('',views.getAuthors),
    path('create/',views.createAuthor),
    path('delete/<int:id>',views.deleteAuthor),
    path('update/<int:id>',views.updateAuthor),
    path('accounts/',include('django.contrib.auth.urls')),
    #path('logout/',views.logout)
    path('accounts/logout/',auth_views.LogoutView.as_view(),name='logout'),
    ]
