from studentsummary.models import Topic
from rest_framework import viewsets, permissions
from .serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    # a query that grabs all the Questions
    queryset = Topic.objects.all()
    # will change later so a user can only access their own questions
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TopicSerializer