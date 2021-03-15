"""
    sounds.py

   Written by:
        Roll   Name                SRN
        __________________________________
        08     Aryan V S           PES1UG20CS083
        09     Aryansh Bhargavan   PES1UG20CS084
        50     Chetan Gurram       PES1UG20CS112
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
