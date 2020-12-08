from django.db import models
import datetime
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField()

    def get_name(self) -> str:
        return self.name

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def get_status(self) -> bool:
        return self.status

    def unlock(self) -> None:
        self.status = True


class Question(models.Model):
    """
    A Math Question in an assignment/assessment.

    === Public Attributes ===
    id: the id of this question
    prompt: the text of this question
    topic_type: the topic type for this question

    === Representation Invariants ===
    question_prompt is not the empty string
    The topic should already in the database. 

    """

    question_prompt = models.CharField(max_length=200)
    topic_type = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0.0)

    def __str__(self) -> str:  
        """
        Return a string representation of this question including the
        text of the question. 
        """
        return self.question_prompt

    def is_topic(self, topic: str) -> bool:
        """
        Return true if the question is of topic <topic>. Return False if
        it is not.

        === Precondition ===
        topic is not empty and formatted in the same way as topic_type
        """
        return self.topic_type == topic

    def get_topic(self) -> str:
        """
        Return the type of question topic of this question.

        """
        return self.topic_type


class Note(models.Model):
    """A note for a student, represented as a string.

    === Private Attributes ===
    _notes:
        A string that contains notes that a student can receive and that
        a student can modify

    === Representation Invariants===
    - len(_notes) <= 250 (less than or equal to 250 characters)
    """
    _notes: str
    _notes = models.CharField(max_length=250)
    topic_type = models.CharField(max_length=200, default="")

    def get_notes(self) -> str:
        """Return the _notes attribute
        """
        return self._notes

    def set_notes(self, message) -> None:
        """Set the _notes attribute to <message>
        Preconditions:
            - len(message) <= 250
        """
        if len(message) <= 250:
            self._notes = message

    def modify_notes(self, message) -> None:
        """Add <message> to the end of the _notes attribute
        Preconditions:
            - len(self._notes) + len(message) <= 250
        """
        if len(self._notes + message) <= 250:
            self._notes += message


class SuggestedPractice(models.Model):
    """shows suggested questions and topics that they are from
    === Representation Invariants===
    - topic_most_missed is always a key in the question_bank
    """
    question_suggested = models.CharField(max_length=200)
    topic_most_missed = models.CharField(max_length=200)
    suggested_at = models.DateTimeField(auto_now_add=True)


class ProgressTracker(models.Model):
    mark = models.IntegerField()
    topic = models.CharField(max_length=200)
