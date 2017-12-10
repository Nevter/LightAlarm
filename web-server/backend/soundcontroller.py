"""
soundcontroller.py
plays sounds
"""

import os

def play(soundFile):
    print("Playing sound "+soundFile)
    os.system("omxplayer ./backend/sound_files/"+soundFile)
    
    