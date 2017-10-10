from microbit import *
import random

hammer = Image("00000:"
               "99999:"
               "99900:"
               "99900:"
               "00000:")
               
scissor = Image("09090:"
                "09090:"
                "00900:"
                "09090:"
                "09090:")
                
paper = Image("00000:"
              "09990:"
              "09990:"
              "09990:"
              "00000:")
              
pic = [hammer, scissor, paper]

while True:
    if accelerometer.is_gesture("shake"):
        display.show(random.choice(pic))
    sleep(20)
