from microbit import *
import random

# Write your code here :-)
dice = Image("77777:"
             "77777:"
             "77777:"
             "77777:"
             "77777:")

numbers = ["1",
           "2",
           "3",
           "4",
           "5",
           "6",
           ]
while True:
    display.show(dice)
    if accelerometer.was_gesture("shake"):
        display.show(Image.ALL_ARROWS)
        display.scroll(random.choice(numbers), delay=600)
