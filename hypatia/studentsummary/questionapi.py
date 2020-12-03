from studentsummary.models import Question
from rest_framework import viewsets, permissions
from .serializers import QuestionSerializer
from django.http import HttpRequest
from rest_framework import generics
from django.shortcuts import render
from django_filters import rest_framework as filters

# Question Viewset
# this lets us create a full CRUD API w/o having to specifiy specific methods for the functionality
class QuestionFilter(filters.FilterSet):
    class Meta:
        model = Question
        fields = ['topic_type']

class QuestionViewSet(viewsets.ModelViewSet):
    # a query that grabs all the Questions
    queryset = Question.objects.all()
    # will change later so a user can only access their own questions
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter
    filterset_fields = ('topic_type')



    # def get_queryset(self):
    #     """
    #     This filters the questions by topic_type and return the objects with
    #     specific topic_type
    #     """
    #
    #     print(HttpRequest.get_full_path(self.request))
    #     return Question.objects.filter(topic_type="division")
