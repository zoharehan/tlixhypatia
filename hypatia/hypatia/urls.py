"""hypatia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from users import views as user_views
from django.contrib import admin

from django.urls import path, include  # Django REST setup
from django.contrib.auth.models import User  # Django REST setup
from rest_framework import routers, serializers, viewsets  # Django REST setup


urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('summary/', include('topicsummary.urls')),
    path('', include('studentsummary.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # browsable API - REST framework's login and logout views
    path('api-auth/', include('rest_framework.urls'))
]
