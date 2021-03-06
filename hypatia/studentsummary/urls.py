from rest_framework import routers
from .questionapi import QuestionViewSet
from .topicapi import TopicViewSet
from .noteapi import NoteViewSet
from .suggestedpracticeapi import SuggestedPracticeViewSet
from .progressapi import ProgressTrackerViewSet
from django.urls import path
from . import views


router = routers.DefaultRouter()
router.register('questionapi/question', QuestionViewSet,
                'question')  
router.register('noteapi/notes', NoteViewSet, 'notes')
router.register('topicapi/topic', TopicViewSet, 'topic')
router.register('suggestedpracticeapi/suggestedpractice',
                SuggestedPracticeViewSet, 'suggestedpractice')
router.register('progressapi/progress', ProgressTrackerViewSet, 'progress')

urlpatterns = router.urls

