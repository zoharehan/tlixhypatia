from django.shortcuts import render
from studentsummary.models import Topic

# Create your views here.


def index(request):
    return render(request, 'topicsummary/index.html')

def topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    return render(request, 'frontend/templates/frontend/index.html', {'topic': topic})
