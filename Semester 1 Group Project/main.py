# """
#     main.py
#
#     Written by:
#         Roll   Name                SRN
#         __________________________________
#         08     Aryan V S           PES1UG20CS083
#         09     Aryansh Bhargavan
#         xx     Chetan Gurram
# """
#
# import init
# import sounds
# import playsound
#
#
# playsound.playsound(sounds.footsteps)
# # playsound.playsound(sounds.footsteps)
# # playsound.playsound(sounds.gravelwalk)
# # playsound.playsound(sounds.headchop)


import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://www.example.com")
content = page.content
soup = bs(content, "lxml")

print(soup.footsteps)