from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('<int:topic_id>/', views.topic, name='topic')
]
