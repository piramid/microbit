from microbit import *
import random

faces = [Image('00000:00000:00900:00000:00000:'),
         Image('00009:00000:00000:00000:90000:'),
         Image('00009:00000:00900:00000:90000:'),
         Image('90009:00000:00900:00000:90009:'),
         Image('90009:00000:00900:00000:90009:'),
         Image('90009:00000:90009:00000:90009:'),
         ]

def RandomImages(n, delay):
    for i in range(0, n):
        display.show(random.choice(faces))
        sleep(delay)
        display.clear()
        sleep(delay)

while True:
    if button_a.was_pressed():
        RandomImages(20, 75)
        rolled = random.choice(faces)
        display.show(rolled)
