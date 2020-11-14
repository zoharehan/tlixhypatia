from rest_framework import routers
from .questionapi import QuestionViewSet
from .noteapi import NoteViewSet

router = routers.DefaultRouter()
router.register('questionapi/question', QuestionViewSet, 'question') # (endpoint/question, viewset)
router.register('noteapi/notes', NoteViewSet, 'notes')

urlpatterns = router.urls