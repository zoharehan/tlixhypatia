"""
=== TLI CSC207 Tests ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Notes class.

Authors: Ali Syed, ...

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Ali Syed"""
import pytest

from topic import Topic
from question import Question

@pytest.fixture
def questions_with_different_types() -> Topic:
    """Create random questions.
    Make sure that the questions attribute for the topic has one question that
    does not match the type of the Topic
    """
    q1 = Question(1, "What is your name?", "Sta247")
    q2 = Question(2, "What is your favorite colour?", "Sta247")
    q3 = Question(3, "When is your birthday?", "Sta247")
    q4 = Question(1, "What happened in 1918?", "HIS101")
    questions = [q1, q2, q3, q4]

    return questions

@pytest.fixture
def random_topic(questions_with_different_types) -> Topic:
    """Create a random topic where questions don't all have the same type.
    """

    return Topic("Statistics", "Sta247", "locked",
                 questions_with_different_types)

# Test Cases for Topics
class Test_Topics:

    def test_get_name(self, random_topic) -> None:
        assert random_topic.get_name() == "Statistics"

    def test_set_name(self, random_topic) -> None:
        random_topic.set_name("Math")
        assert random_topic.get_name() == "Math"

    def test_get_type(self, random_topic) -> None:
        assert random_topic.get_type() == "Sta247"

    def test_get_status(self, random_topic) -> None:
        assert random_topic.get_status() == "locked"

    def test_set_status(self, random_topic) -> None:
        random_topic.set_status("unlocked")
        assert random_topic.get_status() == "unlocked"

    def test_get_questions(self, random_topic) \
            -> None:
        """Make sure that all the questions match the type of the topic."""
        for question in random_topic.get_questions():
            assert question.get_topic() == random_topic.get_type()

if __name__ == '__main__':
    pytest.main(['topic_tests.py'])
