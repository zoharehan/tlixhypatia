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

class Student(models.Model):
    """
    A student user
    === Attributes ===
    name: the name of this student
    student_topics: this student's list of topics
    questions: list of questions the student was assigned
    questions_score: the score on this students questions
    topic_notes: this students note on a topic
    === Representation Invariants ===
    there cannot be a question in questions that has a topic_type \
    not in student_topics
    every key in questions_score must also be in student_topics
    every key in topic_notes must also be in student_topics
    """

    # name: str
    # student_topics: list
    # questions: list
    # questions_score: Dict[Question:int]
    # topic_notes: Dict[str:str] #the topic is the key and the note is the value

    def __init__(self, name):
        self.name = name
        self.student_topics = []
        self.questions = []
        self.questions_score = {}
        self.topic_notes = {}

    # the getter for student's list of topics
    def get_topics(self) -> list:
        return self.student_topics

    # a method that allows a student to add notes to a topic
    def add_topic_notes(self, topic: str) -> str:
        if topic in self.student_topics:
            self.topic_notes[topic] = input("Please enter your note")
            return "your notes were successfully added"
        else:
            return "this topic does not exist"

    # a getter that allows a student to review their notes for a topic
    def get_topic_notes(self, topic: str) -> str:
        if topic not in self.topic_notes:
            return "this topic does not exist"
        else:
            return self.topic_notes[topic]

    # get a question's score; question must have been graded
    def get_score(self, question: Question) -> int:
        if question in self.questions_score:
            return self.questions_score[question]

    # get all questions in a topic
    def get_questions(self, topic: str) -> [Question]:
        all_topic_questions = []
        for question in self.questions:
            if question.topic_type == topic:
                all_topic_questions.append(question)
        return all_topic_questions

class StudentManager(models.Model):
    question_bank = models.ManyToManyField(Question)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.students, self.question_bank
    
    def check_user(self, student: Student) -> bool:
        """
        Return whether the student is in the class. 
        """
        x = self.students.filter(name = student.name)
        return x.exists()
    
    def get_all_questions(self):
        return self.question_bank
    
    def get_questions_topic(self,t: Topic):
        """
        Return all questions for the topic. 
        """
        x = self.questions.filer(topic_type = t)
        return x
    
    def append_question(self, question: Question):
       """
       Add a question from question bank
       """
       self.question_bank.append(question)
       return 

    def delete_question(self,question: Question):
        """
        Delete a question frm question bank
        """
        return self.question_bank.exclude(prompt = question.question_prompt)
    
    def get_all_students(self):
        return self.students


