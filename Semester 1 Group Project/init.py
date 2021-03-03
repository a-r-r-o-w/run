"""
    init.py

    Check for dependencies
    // stuff here
"""

import os
import pkg_resources
import sys
import subprocess

# Module dependencies
requirements = {'playsound', 'bs4'}

# Installed/Available Modules
installed = {i.key for i in pkg_resources.working_set}

# Missing modules
missing = requirements - installed

if missing:
    # Try installing dependencies
    try:
        print("Installing dependencies", *missing)
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
        os.system("cls || clear")
    except:
        print("Dependencies could not be checked/installed. Please try again later!")
        exit()
