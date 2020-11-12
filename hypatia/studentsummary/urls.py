from rest_framework import routers
from .questionapi import QuestionViewSet

router = routers.DefaultRouter()
routers.register('questionapi/question', QuestionViewSet, 'question') # (endpoint/question, viewset)

urlpatters = router.urls