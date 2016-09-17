#!/usr/bin/env python
import random

racer = ''
racers = []
bots = ['Spin Bot', 'Hulk X90', 'Twonky', 'Squash Bot', 'Twitch', 'Zoom Bot', 'Trundle Bot', 'Hammer Bot']
start_pos = [1, 2, 3, 4, 5, 6, 7, 8]
while True:
    racer = raw_input("Racer name: ")
    if str(racer).rstrip() != 'run':
        racers.append(str(racer).rstrip())
    else:
        break
random.shuffle(racers)
random.shuffle(bots)
random.shuffle(start_pos)
race_card = []
for victim in racers:
    mybot = bots.pop()
    mypos = start_pos.pop()
    race_card.append((mypos, victim, mybot))
race_card.sort()
for entry in race_card:
    print(str(entry[0]) + " - " + str(entry[1]) + " - " + str(entry[2]) + "\n")
