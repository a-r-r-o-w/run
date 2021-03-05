"""
    game.py

    // stuff here
"""

# Dependency imports
from bs4 import BeautifulSoup as bs
import os
import time

# Project file imports
import sounds
import player

class Game:
    def __init__(self, xml_file):
        """
            A Game object requires an xml file to setup game configurations

            :param xml_file:
        """

        # XML file with game data
        self.__xml_file = open(xml_file, "r", encoding = "utf-8")

        # Parse the XML file
        self.__parsed_xml = bs(self.__xml_file, "lxml")

        # Game locations
        self.__locations = dict()
        self.__set_locations()

        # Sound files
        self.__sounds = dict()
        self.__set_sound_files()

        # Game player
        self.__player = player.Player(0)

        # Text to display on screen
        self.__text = []
        self.__text_display_delay = 0.02

    def __set_locations(self):
        """
            Sets up location configurations of game
            Adds location by creating attributes with the same name as the location configurations
            in xml file at runtime

            :return: None
        """

        locations = self.__parsed_xml.find_all("location")

        for location in locations:
            lid  = location ["id"]
            name = location.find("name").text

            interactions = dict()
            for interaction in location.find_all("interaction"):
                iid      = interaction ["id"]
                icontent = interaction.content.text

                choices = dict()
                for choice in interaction.find_all("choice"):
                    cid           = choice ["id"]
                    choices [cid] = choice.text

                responses = dict()
                for response in interaction.find_all("response"):
                    rid    = response ["id"]
                    rloc   = response ["location"]
                    rsound = response.find("play")

                    if rsound:
                        rsound = rsound["name"]

                    responses [rid] = {
                        "loc"     : rloc,
                        "sounds"  : rsound,
                        "content" : response.text
                    }

                interactions [iid] = {
                    "content"  : icontent,
                    "choices"  : choices,
                    "response" : responses
                }

            self.__locations = {
                "id" : lid,
                "name" : name,
                "interactions" : interactions
            }

    def __set_sound_files(self):
        """
            Sets up sound configurations of game
            Adds sounds by creating attributes with the same name as the sound configurations
            in xml file at runtime

            :return: None
        """

        for sound in self.__parsed_xml.configurations.sounds.find_all("sound"):
            name = sound.find("name").text.strip()
            file = sound.find("file").text.strip()
            self.__sounds[name] = sounds.Sound(file)

    @staticmethod
    def clear_screen():
        """
            Clears the terminal screen

            :return: None
        """

        os.system("cls || clear")

    def start(self):
        while self.event():
            self.clear_screen()
            self.print_screen()
            time.sleep(5)
            break

    def event(self):
        loc = self.__player.location

        if loc == "-1":
            return False

        self.__text = [self.__locations["interactions"]["1"]["content"]]

        return True

    def print_screen(self):
        """
            The presently stored string data is printed onto screen and set to empty

            :return: None
        """

        print(" {:-<100} ".format(""), flush = True)
        for line in self.__text:
            string = "| {0:<98} |".format(line)

            for c in string:
                print(c, end = "", flush = True)
                if c != " ":
                    time.sleep(self.__text_display_delay)
            print()
        print(" {:-<100} ".format(""), flush = True)

        self.__text = []
