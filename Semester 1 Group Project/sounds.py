"""
    sounds.py

   // stuff here
"""

# Dependency imports
from playsound import playsound

class Sound:
    def __init__(self, file):
        self.file = file
        self.check_existence()

    # Check for the existence of sound file
    def check_existence(self):
        if not isinstance(self.file, str):
            raise TypeError("File must be provided as a string")

    def play(self):
        playsound(self.file)
