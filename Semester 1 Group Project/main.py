"""
    ██████╗░     ██╗░░░██╗      ███╗░░██╗
    ██╔══██╗     ██║░░░██║      ████╗░██║
    ██████╔╝     ██║░░░██║      ██╔██╗██║
    ██╔══██╗     ██║░░░██║      ██║╚████║
    ██║░░██║     ╚██████╔╝      ██║░╚███║
    ╚═╝░░╚═╝     ░╚═════╝░      ╚═╝░░╚══╝

    main.py

    The program is expected to be running on a Windows/Linux terminal.

    Written by:
        Roll   Name                SRN
        __________________________________
        08     Aryan V S           PES1UG20CS083
        09     Aryansh Bhargavan   PES1UG20CS084
        xx     Chetan Gurram       PES1UG20CS
"""

# Project file imports
import init
import game

# create game object by passing in xml configuration file
Game = game.Game("config.xml")

Game.start()
Game.end()
