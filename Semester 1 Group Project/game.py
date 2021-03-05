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
        self.__player = player.Player("1")

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
                    "content"   : icontent,
                    "choices"   : choices,
                    "responses" : responses
                }

            self.__locations = {
                "id"           : lid,
                "name"         : name,
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

    @staticmethod
    def __blank_line(count):
        """
            Prints a formatted blank line onto screen

            :return: None
        """

        for i in range(count):
            print("| {:<98} |".format(""), flush = True)

    def start(self):

        # Display startup screen
        self.clear_screen()
        print(" {:-<100} ".format(""), flush = True)
        Game.Run()
        Game.__blank_line(3)
        print("| Please wait! Initializing", end = "", flush = True)

        for i in range(3):
            for j in range(3):
                time.sleep(0.3)
                print(".", end = "", flush = True)
                time.sleep(0.3)
            if i != 2:
                print("\b\b\b   \b\b\b", end = "", flush = True)

        print("{:70} |".format(""))
        Game.__blank_line(3)
        print("| {0:98} |".format(" ► Press X to begin game"), flush = True)
        print("| {0:98} |".format(" ► Press any to exit game"), flush = True)
        Game.__blank_line(1)
        print(">>> ", end = "", flush = True)
        key = input()
        Game.__blank_line(1)

        if key == "X" or key == 'x':
            print("| {:98} |".format(""), flush = True)
            print(" {:-<100} ".format(""), flush = True)
            time.sleep(2)
        else:
            Game.clear_screen()
            self.end()

        while True:
            self.event()
            Game.clear_screen()

            print(" {:-<100} ".format(""), flush = True)

            self.print_screen()
            time.sleep(1)

            Game.__blank_line(1)
            self.__interact()
            Game.__blank_line(1)

            print(" {:-<100} ".format(""), flush = True)
            time.sleep(2)

            Game.clear_screen()

            print(" {:-<100} ".format(""), flush = True)
            self.print_screen()

            Game.__blank_line(1)
            print("| {0:<98} |".format("Press any key to continue"))
            Game.__blank_line(1)
            input()
            print(" {:-<100} ".format(""), flush = True)
            time.sleep(2)


    @staticmethod
    def end():
        exit()

    def event(self):
        loc = self.__player.location

        if loc == "-1":
            self.end()

        self.__text  = [line.strip() for line in self.__locations["interactions"][loc]["content"].split("\n")]
        for choice in self.__locations["interactions"][loc]["choices"]:
            c = self.__locations["interactions"][loc]["choices"][choice].strip()

            string = "(" + choice + ") " + c
            self.__text += [string]

        return True

    def print_screen(self):
        """
            The presently stored string data is printed onto screen and set to empty

            :return: None
        """

        run = ["█▄▄▄▄  ▄      ▄", "█  ▄▀   █      █", " █▀▀▌ █   █ ██   █",
               " █  █ █   █ █ █  █", "   █  █▄ ▄█ █  █ █", "  ▀    ▀▀▀  █   ██"]

        for line in run:
            print("| {:^98} |".format(line), flush = True)
        Game.__blank_line(1)

        for line in self.__text:
            string = "| {0:<98} |".format(line)

            for c in string:
                print(c, end = "", flush = True)
                if c != " ":
                    time.sleep(self.__text_display_delay)

            print(flush = True)

        self.__text = []

    def __interact(self):
        print(">>> ", end = "", flush = True)
        key = input()

        loc = self.__player.location

        if key not in self.__locations["interactions"][loc]["responses"].keys():
            Game.clear_screen()
            self.end()

        response = self.__locations["interactions"][loc]["responses"][key]
        self.__player.set_location(response["loc"])
        self.__text = [line.strip() for line in response["content"].split("\n")]

    @staticmethod
    def Run():
        run = ["██████╗░     ██╗░░░██╗      ███╗░░██╗", "██╔══██╗     ██║░░░██║      ████╗░██║",
               "██████╔╝     ██║░░░██║      ██╔██╗██║", "██╔══██╗     ██║░░░██║      ██║╚████║",
               "██║░░██║     ╚██████╔╝      ██║░╚███║", "╚═╝░░╚═╝     ░╚═════╝░      ╚═╝░░╚══╝"]

        for line in run:
            print("| {0:^98} |".format(line), flush = True)
        print("| {:<98} |".format("Made with ♥ by:"))
        print("| {:<98} |".format("    Aryan V S"))
        print("| {:<98} |".format("    Aryansh Bhargavan"))
        print("| {:<98} |".format("    Chetan Gurram"))
