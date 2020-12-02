from studentsummary.models import ProgressTracker
from rest_framework import viewsets, permissions
from .serializers import ProgressTrackerSerializer
from rest_framework.decorators import action
from django.http import HttpResponse


class ProgressTrackerViewSet(viewsets.ModelViewSet):
    # a query that grabs all the progresses
    queryset = ProgressTracker.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProgressTrackerSerializer

    def list(self, request):
        # queryset = User.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        print("responded")
        if request.method == 'GET':
            return HttpResponse("GET Request.")
        elif request.method == 'POST':
            print(request.body)
            return HttpResponse("POST")

        else: 
            return HttpResponse("other requests")

    # when you hit a URL.