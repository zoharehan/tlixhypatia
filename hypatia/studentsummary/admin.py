from django.contrib import admin
from .models import Question
from .models import SuggestedPractice

# Register your models here.
admin.site.register(Question) #registered the Question class for the database
admin.site.register(SuggestedPractice)
