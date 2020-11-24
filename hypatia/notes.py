"""TLI CSC207 Project

Authors: Ali Syed

All of the files in this directory and all subdirectories are:
Copyright (c) Ali Syed

=== Module Description ===

This file contains the Notes class, one of the entities of our class.
"""

class Note:
    """A note for a student, represented as a string.

    === Private Attributes ===
    _notes:
        A string that contains notes that a student can receive and that
        a student can modify

    === Representation Invariants===
    - len(_notes) <= 250 (less than or equal to 250 characters)
    """
    _notes: str

    def __init__(self, message) -> None:
        """Initialize this note with <message>

        Preconditions:
            - len(message) <= 250
        """
        self._notes = message

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
