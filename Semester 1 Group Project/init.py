"""
    init.py

    // stuff here
"""

import os
import pkg_resources
import sys
import subprocess

# Check for dependencies
requirements = {'playsound', 'bs4'}
installed = {i.key for i in pkg_resources.working_set}

missing = requirements - installed

if missing:
    try:
        print("Installing dependencies", *missing)
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
        os.system("cls || clear")
    except:
        print("Dependencies could not be checked/installed. Please try again later!")
        exit()
