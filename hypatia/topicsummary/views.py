from django.shortcuts import render
from studentsummary.models import Topic


def index(request):
    return render(request, 'topicsummary/index.html')

def topic(request, topic_name):
    topic = Topic.objects.get(name=topic_name)
    return render(request, 'frontend/templates/frontend/index.html', {'topic': topic})
