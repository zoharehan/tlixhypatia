from rest_framework import routers
from .questionapi import QuestionViewSet

router = routers.DefaultRouter()
router.register('questionapi/question', QuestionViewSet, 'question') # (endpoint/question, viewset)

urlpatterns = router.urls
                                    