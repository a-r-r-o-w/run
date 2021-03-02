"""
    sounds.py

   // stuff here
"""

class Sounds:
    def __init__(self, sound_file):
        self.file = sound_file
        def fn():
            return sound_file
        setattr(Sounds, sound_file, fn)
        self.check_existence()

    # Check for the existence of sound file
    def check_existence(self):
        if not isinstance(self.file, str):
            raise TypeError("File must be provided as a string")

sound_files = ["footsteps.wav", "gravelwalk.wav", "headchop.wav"]

sounds = list(map(Sounds, sound_files))

# footsteps  = sounds [0].file
# gravelwalk = sounds [1].file
# headchop   = sounds [2].file

