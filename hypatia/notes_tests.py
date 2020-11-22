"""CSC148 Assignment 1: Sample tests

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Notes class.

Authors: Ali Syed, ...

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Ali Syed"""
import pytest

from notes import Note


# Test Cases for Notes
class Test_Notes:

    def test_get_notes(self) -> None:
        topic_notes = Note("Hey there!!")
        str = "Hey there!!";
        assert topic_notes.get_notes() == str

    def test_set_notes(self):

        temp_str = "Bob"
        short_str = "Hello, my name is Ali Syed and I am a grade 5 math " \
                    "student. I need to learn a lot of math!!!"
        long_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
                   "sed do eiusmod tempor incididunt ut labore et dolore magna " \
                   "aliqua. Ut enim ad minim veniam, quis nostrud exercitation " \
                   "ullamco laboris nisi ut aliquip ex ea commodo consequat. " \
                   "Duis aute irure dolor in reprehenderit in voluptate velit " \
                   "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" \
                   " occaecat cupidatat non proident, sunt in culpa qui officia "

        #Testing if it sets note with <message> <= 250 words
        notes = Note()
        notes.set_notes(short_str)
        assert notes.get_notes() == short_str

        #Testing if it sets note with <message> > 250 words
        notes = Note(temp_str)
        notes.set_notes(long_str)
        assert notes.get_notes() == temp_str

    def test_set_notes(self):

        temp_str = "Bob"
        short_str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing " \
                     "elit, sed do eiusmod tempor incididunt ut labore et " \
                     "dolore magna aliqua. Ut enim ad minim veniam, quis " \
                     "nostrud exercitation ullamco laboris nisi ut aliquip " \
                     "ex ea commodo consequat."
        short_str2 = "Lorem ipsum dolor sit amet, consectetur adipiscing " \
                     "elit, sed do eiusmod tempor incididunt ut labore et " \
                     "dolore magna aliqua. Ut enim ad minim veniam, quis " \
                     "nostrud exercitation ullamco laboris nisi ut aliquip " \
                     "ex ea commodo consequat."

        #Testing if it sets note with <message> <= 250 words
        notes = Note(temp_str)
        notes.modify_notes(short_str1)
        assert notes.get_notes() == temp_str + short_str1

        #Testing if it sets note with <message> > 250 words
        notes = Note(short_str1)
        notes.modify_notes(short_str2)
        assert notes.get_notes() == short_str1


if __name__ == '__main__':
    pytest.main(['notes_tests.py'])
