from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def detail(request,topic_id):
#     return HttpResponse("You're looking at topic %s." % topic_id)

# def results(request,topic_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % topic_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % topic_id)