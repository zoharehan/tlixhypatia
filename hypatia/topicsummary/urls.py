from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('<str:topic_name>/', views.topic, name='topic')
]
