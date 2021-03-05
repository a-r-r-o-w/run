"""
    main.py

    The program is expected to be running on a Windows/Linux terminal.

    Written by:
        Roll   Name                SRN
        __________________________________
        08     Aryan V S           PES1UG20CS083
        09     Aryansh Bhargavan
        xx     Chetan Gurram
"""

# Project file imports
import init
import game

# create game object by passing in xml configuration file
Game = game.Game("config.xml")

Game.start()
