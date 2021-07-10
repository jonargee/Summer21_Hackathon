import pygame
from pygame import mixer

# code adapted form GeeksforGeeks tutorial about pygames audio playing features

# starting mixer
mixer.init()

# loading the song
# music is royalty free from https://www.pygame.org/docs/ref/mixer.html (placeholder for now)
mixer.music.load("Free Game Loop.wav")

# volume setting
volume_lvl = 0.5
mixer.music.set_volume(volume_lvl)

# playing the music
mixer.music.play(-1)                        # sets the music to play indefinitely

# interacting with music settings while game is running
while True:

    # while game is running, wait for specific inputs
    music_cmd = input("")
    toggle_set = 0

    # controlling music play
    if music_cmd == 'm':
        mixer.music.pause()
        toggle_set = 1
    elif music_cmd == 'n':
        mixer.music.unpause()
        toggle_set = 0
    elif music_cmd == 'stop':               # not sure if this is necessary
        mixer.music.stop()
        break

    #  volume control settings
    elif music_cmd == 'k':                  # increases volume when k is entered
        volume_lvl = volume_lvl + 0.1
        mixer.music.set_volume(volume_lvl)
    elif music_cmd == 'l':                  # decreased volume when l is entered
        volume_lvl = volume_lvl - 0.1
        mixer.music.set_volume(volume_lvl)

