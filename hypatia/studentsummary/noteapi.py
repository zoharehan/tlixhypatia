from studentsummary.models import Note
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer
from django_filters import rest_framework as filters


class NoteFilter(filters.FilterSet):
    class Meta:
        model = Note
        fields = ['topic_type']


class NoteViewSet(viewsets.ModelViewSet):
  
    queryset = Note.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NoteSerializer
    filter_class = NoteFilter
    filterset_fields = ('topic_type')
