from studentsummary.models import Question
from rest_framework import viewsets, permissions
from .serializers import QuestionSerializer
from django.http import HttpRequest
from rest_framework import generics
from django.shortcuts import render
from django_filters import rest_framework as filters

class QuestionFilter(filters.FilterSet):
    class Meta:
        model = Question
        fields = ['topic_type']

class QuestionViewSet(viewsets.ModelViewSet):
   
    queryset = Question.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter
    filterset_fields = ('topic_type')
