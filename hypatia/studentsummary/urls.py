from rest_framework import routers
from .questionapi import QuestionViewSet
from .suggestedpracticeapi import SuggestedPracticeViewSet

router = routers.DefaultRouter()
router.register('questionapi/question', QuestionViewSet, 'question') # (endpoint/question, viewset)
router.register('suggestedpracticeapi/suggestedpractice', SuggestedPracticeViewSet, 'suggestedpractice')

urlpatterns = router.urls