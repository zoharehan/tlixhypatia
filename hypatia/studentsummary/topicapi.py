from studentsummary.models import Topic
from rest_framework import viewsets, permissions
from .serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    # a query that grabs all the Questions
    queryset = Topic.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TopicSerializer