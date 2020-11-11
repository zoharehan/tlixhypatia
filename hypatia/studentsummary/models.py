from django.db import models

class StudentManager(models.Model):
    question_bank = models.ManyToManyField(Question)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.students, self.questions
    
    def check_user(self, Student) -> bool:
        """
        Return whether the student is in the class. 
        """
        x = self.students.filter(name = Student.name)
        if len(x) != 0:
            return True
        return False
    
    def get_all_questions(self):
        return self.question_bank
    
    def get_questions_topic(self,Topic):
        """
        Return all questions for the topic. 
        """
        x = self.questions.filer(topic = Topic)
        return x
    
    def append_question(self,Question):
        


