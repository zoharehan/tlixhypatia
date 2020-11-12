from django.shortcuts import render

# Create your views here.
# this is where we want to point to the template (React)

def index(request):
    return render(request, 'frontend/index.html')