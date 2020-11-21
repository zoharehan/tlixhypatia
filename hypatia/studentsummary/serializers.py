from rest_framework import serializers
from studentsummary.models import Question, Note, Topic, SuggestedPractice, ProgressTracker

# Question Serializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

# Note Serializer


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

# Topic Serializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

# SuggestedPractice Serializer


class SuggestedPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestedPractice
        fields = '__all__'

# ProgressTracker Serializer


class ProgressTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTracker
        fields = '__all__'
