from studentsummary.models import Question
from rest_framework import viewsets, permissions
from .serializers import QuestionSerializer

# Question Viewset
# this lets us create a full CRUD API w/o having to specifiy specific methods for the functionality

class QuestionViewSet(viewsets.ModelViewSet):
    # a query that grabs all the Questions
    queryset = Question.objects.all()
    # will change later so a user can only access their own questions
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer
