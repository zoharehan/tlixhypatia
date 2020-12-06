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
                'question')  # (endpoint/question, viewset)
router.register('noteapi/notes', NoteViewSet, 'notes')
router.register('topicapi/topic', TopicViewSet, 'topic')
router.register('suggestedpracticeapi/suggestedpractice',
                SuggestedPracticeViewSet, 'suggestedpractice')
router.register('progressapi/progress', ProgressTrackerViewSet, 'progress')

urlpatterns = router.urls


# urlpatterns = [
#     path('',views.index,name= "index"),

#     path('<int:topic_id>/',views.detail,name = 'detail'),
#     path('<int:topic_id>/results/',views.results,name = 'results'),
#     path('<int:topic_id>/vote/',views.vote,name='vote'),
# ]
