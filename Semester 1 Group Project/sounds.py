"""
    sounds.py

   // stuff here
"""

#
class Sound:
    def __init__(self, sound_file):
        self.file = sound_file
        self.check_existence()
        setattr(Sound, sound_file [:-4], sound_file)

    # Check for the existence of sound file
    def check_existence(self):
        if not isinstance(self.file, str):
            raise TypeError("File must be provided as a string")


sound_files = ["footsteps.wav", "gravelwalk.wav", "headchop.wav"]

list(map(Sound, sound_files))