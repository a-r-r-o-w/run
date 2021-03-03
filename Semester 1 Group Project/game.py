"""
    game.py

    // stuff here
"""

# Dependency imports
from bs4 import BeautifulSoup as bs

# Project file imports
import sounds
import player

class Game:
    def __init__(self, xml_file):
        # XML file with game data
        self.xml_file = open(xml_file, "r", encoding = "utf-8")

        # Parse the XML file
        self.parsed_xml = bs(self.xml_file, "lxml")

        # Game locations
        self.locations = dict()
        self.set_locations()

        # Sound files
        self.sounds = dict()
        self.set_sound_files()

        # Game player
        self.player = player.Player(0)

    def set_locations(self):
        location_data = self.parsed_xml.locations.find_all("location")
        print(location_data)

    def set_sound_files(self):
        for sound in self.parsed_xml.sounds.find_all("sound"):
            name = sound.find("name").text.strip()
            file = sound.find("file").text.strip()
            self.sounds[name] = sounds.Sound(file)

    def start(self):
        pass
