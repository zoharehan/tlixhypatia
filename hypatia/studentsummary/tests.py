from django.test import TestCase
from django.urls import reverse
from .models import Question, Topic
# Create your tests here.

class TopicModelTests(TestCase):
    def test_get_topic_name(self):
        topic = Topic(name = "Algebra",status = False)
        self.assertIs(topic.get_name(),"Algebra")

    def test_set_name(self):
        topic = Topic(name = "Algebra",status = False)
        topic.set_name("Equation")
        self.assertIs(topic.name, "Equation")

    def test_get_status(self):
        topic = Topic(name = "Algebra",status = False)
        self.assertIs(topic.get_status(),False)
        topic = Topic(name = "Algebra",status = True)
        self.assertIs(topic.get_status(),True)

    def test_unlock(self):
        topic = Topic(name = "Algebra",status = False)
        topic.unlock()
        self.assertIs(topic.status,True)

def create_question(question_prompt, topic_type):
    """
    Create a question with the given `question_id` and 'question prompt',
    and 'topic_type'.
    """
    return Question.objects.create(question_prompt=question_prompt, topic_type=topic_type)


class QuestionTests(TestCase):
    def test_str_method(self):
        """
        Testing the str method in the Question class.
        """
        question = create_question(question_prompt="divide the pie", topic_type="division")
        self.assertEqual(question.__str__(), "divide the pie")

    def test_is_topic_method_1(self):
        """
        Testing the is_topic method in the Question class.
        """
        question = create_question(question_prompt="divide the cake", topic_type="division")
        self.assertEqual(question.is_topic("division"), True)

    def test_is_topic_method_2(self):
        """
        Testing the is_topic method in the Question class.
        """
        question = create_question(question_prompt="divide the cheese", topic_type="division")
        self.assertEqual(question.is_topic("addition"), False)

    def test_get_topic_method(self):
        """
        Testing the is_topic method in the Question class.
        """
        question = create_question(question_prompt="divide the pie", topic_type="division")
        self.assertEqual(question.get_topic(), "division")

