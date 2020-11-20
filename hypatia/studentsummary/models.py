from django.db import models
import datetime
from django.utils import timezone

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

class Topic(models.Model):
    name = models.CharField(max_length = 100)
    status = models.BooleanField()
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self,new_name: str) -> None:
        self.name = new_name
    
    def get_status(self) -> bool:
        return self.status
    
    def unlock(self) -> None:
        self.status = True 


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

    name = models.CharField(max_length = 100)
    questions = []
    topics = []
    score = []

    def get_topics(self):
        return topics

    # # a method that allows a student to add notes to a topic
    # def add_topic_notes(self, topic: str) -> str:
    #     if topic in self.student_topics:
    #         self.topic_notes[topic] = input("Please enter your note")
    #         return "your notes were successfully added"
    #     else:
    #         return "this topic does not exist"

    # # a getter that allows a student to review their notes for a topic
    # def get_topic_notes(self, topic: str) -> str:
    #     if topic not in self.topic_notes:
    #         return "this topic does not exist"
    #     else:
    #         return self.topic_notes[topic]

    # get a question's score; question must have been graded
    # def get_score(self, question: Question) -> int:
    #     if question in self.questions_score:
    #         return self.questions_score[question]

    # # get all questions in a topic
    # def get_questions(self, topic: str) -> [Question]:
    #     all_topic_questions = []
    #     for question in self.questions:
    #         if question.topic_type == topic:
    #             all_topic_questions.append(question)
    #     return all_topic_questions

# class Studentmanager(models.Model):
#     question_bank = models.ManyToManyField(Question)
#     #students = models.ManyToManyField(Student)

#     def __str__(self):
#         return self.question_bank   # self.students,
    
#     # def check_user(self, student: Student) -> bool:
#     #     """
#     #     Return whether the student is in the class. 
#     #     """
#     #     x = self.students.filter(name = student.name)
#     #     return x.exists()
    
#     def get_all_questions(self):
#         return self.question_bank
    
#     # def get_questions_topic(self,t: Topic):
#     #     """
#     #     Return all questions for the topic. 
#     #     """
#     #     x = self.questions.filer(topic_type = t)
#     #     return x
    
#     def append_question(self, question: Question):
#        """
#        Add a question from question bank
#        """
#        self.question_bank.append(question)
#        return 

#     def delete_question(self,question: Question):
#         """
#         Delete a question frm question bank
#         """
#         return self.question_bank.exclude(prompt = question.question_prompt)
    
#     # def get_all_students(self):
#     #     return self.students

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
                


