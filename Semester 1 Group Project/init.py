"""
    init.py

    Check for dependencies

    Written by:
        Roll   Name                SRN
        __________________________________
        08     Aryan V S           PES1UG20CS083
        09     Aryansh Bhargavan   PES1UG20CS084
        50     Chetan Gurram       PES1UG20CS112
"""

import os
import pkg_resources
import sys
import subprocess
import time

def setup():
    # Module dependencies
    requirements = {'playsound', 'bs4', 'lxml'}

    # Installed/Available Modules
    installed = {i.key for i in pkg_resources.working_set}

    # Missing modules
    missing = requirements - installed

    if missing:
        # Try installing dependencies
        try:
            print("Installing dependencies", *missing)
            print()
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
            print()
            print("Dependencies installed successfully!")
            time.sleep(2)

        # Installation unsuccessful
        except:
            print("Dependencies could not be checked/installed. Please try again later!")
            exit()
