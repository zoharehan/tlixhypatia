from studentsummary.models import ProgressTracker
from rest_framework import viewsets, permissions
from .serializers import ProgressTrackerSerializer

# ProgressTracker Viewset
# this lets us create a full CRUD API w/o having to specify specific methods for the functionality


class ProgressTrackerViewSet(viewsets.ModelViewSet):
    # a query that grabs all the progresses
    queryset = ProgressTracker.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProgressTrackerSerializer
