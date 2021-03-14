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
    __text_length = 100

    __text_display_delay = 0.02

    __logo1 = ["██████╗░     ██╗░░░██╗      ███╗░░██╗", "██╔══██╗     ██║░░░██║      ████╗░██║",
               "██████╔╝     ██║░░░██║      ██╔██╗██║", "██╔══██╗     ██║░░░██║      ██║╚████║",
               "██║░░██║     ╚██████╔╝      ██║░╚███║", "╚═╝░░╚═╝     ░╚═════╝░      ╚═╝░░╚══╝"]

    __logo2 = ["█▄▄▄▄  ▄      ▄", "█  ▄▀   █      █", " █▀▀▌ █   █ ██   █",
               " █  █ █   █ █ █  █", "   █  █▄ ▄█ █  █ █", "  ▀    ▀▀▀  █   ██"]

    __has_ended = False

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
            name = location.find("name").text.strip()

            interactions = dict()
            for interaction in location.find_all("interaction"):
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

                interactions = {
                    "content"   : icontent,
                    "choices"   : choices,
                    "responses" : responses
                }

            self.__locations [lid] = {
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
    def __clear_screen():
        """
            Clears the terminal screen

            :return: None
        """

        os.system("cls || clear")

    @staticmethod
    def __pretty_print(string, indent = "<"):
        """
            Formats a string in the predetermined pattern for pretty printing onto screen

            :param string: str to be formatted
            :return: None
        """

        print("| {0:{indent}{size}} |".format(string, indent = indent, size = Game.__text_length), flush = True)

    @staticmethod
    def __boxify(f):
        print(" {:-<{size}} ".format("", size = Game.__text_length + 2), flush = True)
        f()
        print(" {:-<{size}} ".format("", size = Game.__text_length + 2), flush = True)

    @staticmethod
    def __startup_screen():
        """
            Displays startup screen

            :return: None
        """

        for line in Game.__logo1:
            Game.__pretty_print(line, "^")

        Game.__pretty_print("Made with ♥ by:")
        Game.__pretty_print("    Aryan V S")
        Game.__pretty_print("    Aryansh Bhargavan")
        Game.__pretty_print("    Chetan Gurram")
        Game.__pretty_print("")
        Game.__pretty_print("")
        Game.__pretty_print("")
        print("{0}".format(input(">>> Press Enter to continue")))
        Game.__pretty_print("")

    def start(self):
        """
            Starts the main game loop which handles game events and interactions

            :return: None
        """

        # Display startup screen
        Game.__clear_screen()
        Game.__boxify(self.__startup_screen)

        # Game loop handling different events
        while True:

            # Clear Game screen
            Game.__clear_screen()

            # Setup current event
            Game.__boxify(self.__event)

            time.sleep(2)

            # Clear Game screen
            Game.__clear_screen()

            # Print current event response data based on interaction
            Game.__boxify(self.__respond)

            time.sleep(2)

    def __event(self):
        loc = self.__player.location

        if loc == "-1":
            Game.end()

        content = self.__locations[loc]["interactions"]["content"]
        choices = self.__locations[loc]["interactions"]["choices"]

        self.__text  = [line.strip() for line in content.split("\n")]
        for choice in choices:
            c = choices[choice].strip()

            string = "(" + choice + ") " + c
            self.__text += [string]

        # Print current event data onto screen
        self.__print_screen()

        # Interact with user based on current event data
        Game.__pretty_print("")
        self.__interact()
        Game.__pretty_print("")

    def __respond(self):
        self.__print_screen()
        Game.__pretty_print("")
        print("{0}".format(input(">>> Press Enter to continue")))
        Game.__pretty_print("")

    def __print_screen(self):
        """
            The presently stored string data is printed onto screen and set to empty

            :return: None
        """

        for line in Game.__logo2:
            Game.__pretty_print(line, "^")

        Game.__pretty_print("")

        for line in self.__text:
            string = "| {0:<100} |".format(line)

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

        if key not in self.__locations[loc]["interactions"]["responses"].keys():
            Game.__clear_screen()
            self.end()

        response = self.__locations[loc]["interactions"]["responses"][key]
        self.__player.set_location(response["loc"])
        self.__text = [line.strip() for line in response["content"].split("\n")]

    @staticmethod
    def end():
        Game.__clear_screen()
        exit()
