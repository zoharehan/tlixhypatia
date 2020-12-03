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
    # This tells Django what type of data each field holds
    # similar to the _init_ but for database (check the tutorial to be sure)
    # id: int
    # question_prompt: str
    # topic_type: str

    # db give each Question object an id , so I will add a time field instead

    question_prompt = models.CharField(max_length=200)
    topic_type = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # topic_type = models.CharField(max_length = 200)
    # time will be added automatically
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0.0)

    # maybe have the date as the question_id? or have a time submitted variable?

    def __str__(self) -> str:  # doubles as the getter for question
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


class Student(models.Model):
    """
    A student user
    === Attributes ===
    name: the name of this student
    topics: this student's list of topics
    questions: list of questions the student was assigned
    score: the score on this students questions

    === Representation Invariants ===
    there cannot be a question in questions that has a topic_type \
    not in student_topics
    every key in questions_score must also be in student_topics
    every key in topic_notes must also be in student_topics
    """

    name = models.CharField(max_length=100)
    questions = []
    topics = []
    score = []

    def get_topics(self):
        return topics
    # def add_topic


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
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
