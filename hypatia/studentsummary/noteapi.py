from studentsummary.models import Note
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer

# Note Viewset
# this lets us create a full CRUD API w/o having to specifiy specific methods for the functionality

class NoteViewSet(viewsets.ModelViewSet):
    # a query that grabs all the notes
    queryset = Note.objects.all()
    # might change later to change permissions of which users can access which notes
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NoteSerializer