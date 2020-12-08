from studentsummary.models import SuggestedPractice
from rest_framework import viewsets, permissions
from .serializers import SuggestedPracticeSerializer
from django_filters import rest_framework as filters


# SuggestedPractice Viewset
# this lets us create a full CRUD API w/o having to specifiy specific methods for the functionality
class SuggestedPracticeFilter(filters.FilterSet):
    class Meta:
        model = SuggestedPractice
        fields = ['topic_most_missed']

class SuggestedPracticeViewSet(viewsets.ModelViewSet):
    # a query that grabs all the Questions
    queryset = SuggestedPractice.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SuggestedPracticeSerializer
    filter_class = SuggestedPracticeFilter
    filterset_fields = ('topic_most_missed')
