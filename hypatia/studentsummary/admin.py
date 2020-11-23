from django.contrib import admin
from .models import Question, Topic

# Register your models here.
admin.site.register(Question)  # registered the Question class for the database
admin.site.register(Topic)
# admin.site.register(Student)
