#!/usr/bin/python
import random

# RoboRally track tiles (2-sided, 4 tiles)
track_tiles = [('Chop Shop', 'Island'), ('Cross', 'Chess'), ('Exchange', 'Vault'), ('Spin Zone', 'Maelstrom')]
orientation = ['N', 'S', 'E', 'W']

shuffles = random.randint(4, 11)
while shuffles > 0:
    random.shuffle(track_tiles)
    shuffles -= 1

for tile in track_tiles:
    print(str(random.choice(tile)) + " - " + str(random.choice(orientation)) + "\n")
