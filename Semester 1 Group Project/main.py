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
        xx     Chetan Gurram       PES1UG20CS112
"""

# Project file imports
import init
import game

# Run initial setup
init.setup()

# Create Game object
Game = game.Game("config.xml")

# Start Game
Game.start()

# End Game
Game.end()
