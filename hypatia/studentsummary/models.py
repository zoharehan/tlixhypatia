from django.db import models
import datetime
from django.utils import timezone

class Student(models.Model):       # for purpose of testing only 
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.TextField()
    topic = models. CharField(max_length=  100)
    def __str__(self):
        return self.name 

class StudentManager(models.Model):
    question_bank = models.ManyToManyField(Question)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.students, self.question_bank
    
    def check_user(self, Student) -> bool:
        """
        Return whether the student is in the class. 
        """
        x = self.students.filter(name = Student.name)
        return x.exists()
    
    def get_all_questions(self):
        return self.question_bank
    
    def get_questions_topic(self,Topic):
        """
        Return all questions for the topic. 
        """
        x = self.questions.filer(topic = Topic)
        return x
    
   def append_question(self,Question):
       """
       Add a question from question bank
       """
       self.question_bank.append(Question)

    def delete_question(self,Question):
        """
        Delete a question frm question bank
        """
        return self.question_bank.exclude(prompt = Question.prompt)
    
    def get_all_students(self):
        return self.students


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

