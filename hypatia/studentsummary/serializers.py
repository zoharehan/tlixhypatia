from rest_framework import serializers
from studentsummary.models import Question
from studentsummary.models import SuggestedPractice

# Question Serializer
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class SuggestedPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestedPractice
        fields = '__all__'

