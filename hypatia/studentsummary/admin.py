from django.contrib import admin
from .models import Question, Topic

# Register your models here.
admin.site.register(Question)  
admin.site.register(Topic)
