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
    
class SuggestedPractice(models.Model):
    """shows suggested questions and topics that they are from
     === Public Attributes ===
    student:
        a student object used to obtain completed questions and missed topics
        for suggested practice questions
    === Representation Invariants===
    - topic_most_missed is always a key in the question_bank
    """
    question_suggested = models.CharField(max_length=200)
    topic_most_missed = models.CharField(max_length=200)
    suggested_at = models.DateTimeField(auto_now_add=True)

    def get_topic_most_missed(self):
        """return the topic the student is weakest in by calling on
        a method from the StudentPerformance Class"""
        self.topic_most_missed = StudentPerformance(self.student).get_topic_most_missed()
        return self.topic_most_missed

    def get_question(self):
        """return a question object from the question bank by calling on
        StudentManager for the student to practice"""
        li = StudentManager(self.student).get_all_questions()
        for i in li[self.get_topic_most_missed()]:
            if li[self.get_topic_most_missed()] == self.student.get_completed_questions()\
                    or li[self.get_topic_most_missed()] == []:
                return "congratulations, you have finished all your practice!"
            if i not in self.student.get_completed_questions():
                self.question_suggested = i
                return i
    
   
