from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    """
    A Math Question in an assignment/assessment.

    === Public Attributes ===
    id: the id of this question
    prompt: the text of this question
    topic_type: the topic type for this question

    === Representation Invariants ===
    question_prompt is not the empty string

    """
    # This tells Django what type of data each field holds
    # similar to the _init_ but for database (check the tutorial to be sure)
    # id: int
    # question_prompt: str
    # topic_type: str

    # db give each Question object an id , so I will add a time field instead

    question_prompt = models.CharField(max_length=200)
    topic_type = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) #time will be added automatically

    # maybe have the date as the question_id? or have a time submitted variable?

    # def __init__(self, question_id, question_prompt, topic_type) -> None:
    #      # not sure if we need this?
    #      # question id should be automatically generated
    #      self.question_id = question_id
    #      self.question_prompt = question_prompt
    #      self.topic_type = topic_type

    def __str__(self) -> str: #doubles as the getter for question
         """
         Return a string representation of this question including the
         text of the question.
         """
         # adding a __str__() method
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

    # Replaces the init method
    _notes = models.CharField(max_length=250)

    # def __init__(self, message) -> None:
    #     """Initialize this note with <message>
    #     Preconditions:
    #         - len(message) <= 250
    #     """
    #     self._notes = message

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

