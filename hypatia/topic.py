"""TLI CSC207 Project

Authors: Ali Syed

All of the files in this directory and all subdirectories are:
Copyright (c) Ali Syed

=== Module Description ===

This file contains the Topics class.
"""

from typing import List
from question import Question


class Topic:
    """A Topic that a student is taking, and has questions relating to that
    topic.

    === Private Attributes ===
    _name: name of the topic
    _type: type of the topic (related to class [question].topic_type)
    _status: "locked" or "unlocked" status for which topics have been taught
    and those that haven't
    _questions: holds a list of questions relating to that topic

    === Representation Invariants===
    - the _questions List can only have questions of the Question class whose
    topic_type attribute match the _type of the Topic class
    - the type of the topic must be unique (two different topics should have
    the same _type attribute)
    """
    _name: str
    _type: str
    _status: str
    _questions: List[Question]

    def __init__(self, name: str, type: str, status: str,
                 questions: List[Question]) -> None:
        """Initialize Topic with <name>, UNIQUE <type>, status <status>,
         and list of <questions> that should all end up having the same
         topic_type <type>.
        """
        self._name = name
        self._type = type
        self._status = status
        self._questions = []

        for question in questions:
            if question.get_topic() == self._type:
                self._questions.append(question)

    def get_name(self) -> str:
        """Return the name of the topic"""
        return self._name

    def set_name(self, new_name) -> None:
        """Set the name for the topic"""
        self._name = new_name

    def get_questions(self) -> List[Question]:
        """ Return the list of questions
        """
        return self._questions

    def get_type(self) -> str:
        """ Return the unique type of the topic.

        Ali has not put a setter for changing the type, since you ideally
        don't want to change the type for that topic once it has been set.
        If you do want to change the name of the topic, use the _name attribute
        for the topic.
        """
        return self._type

    def get_status(self) -> str:
        """Return the status of the topic (either "locked" or "unlocked")"""
        return self._status

    def set_status(self, new_status) -> None:
        """Set status to <new_status>

        Precondition:
        - <new_status> can only be "locked" or "unlocked"
        """
        self._status = new_status



