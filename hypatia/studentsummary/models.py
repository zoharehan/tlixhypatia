from django.db import models

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